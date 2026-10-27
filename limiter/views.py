from django.shortcuts import render

# Create your views here.
from datetime import timedelta

from django.http import JsonResponse
from django.utils import timezone

from .models import RequestLog


MAX_REQUESTS = 5
TIME_WINDOW = 60  # seconds


def get_client_ip(request):
    """
    Get client's IP address.
    """

    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if forwarded_for:
        ip = forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def home(request):
    return render(request, "limiter/index.html")


def api(request):
    """
    Rate-limited API endpoint.

    Maximum:
        5 requests
        per 60 seconds
        per IP address
    """

    ip = get_client_ip(request)

    current_time = timezone.now()
    window_start = current_time - timedelta(seconds=TIME_WINDOW)

    # Delete old records
    RequestLog.objects.filter(
        ip_address=ip,
        timestamp__lt=window_start
    ).delete()

    # Count requests in current window
    request_count = RequestLog.objects.filter(
        ip_address=ip,
        timestamp__gte=window_start
    ).count()

    # Rate limit exceeded
    if request_count >= MAX_REQUESTS:
        oldest_request = RequestLog.objects.filter(
            ip_address=ip,
            timestamp__gte=window_start
        ).order_by("timestamp").first()

        retry_after = TIME_WINDOW

        if oldest_request:
            elapsed = (current_time - oldest_request.timestamp).total_seconds()
            retry_after = max(1, int(TIME_WINDOW - elapsed))

        return JsonResponse(
            {
                "success": False,
                "message": "Rate limit exceeded",
                "limit": MAX_REQUESTS,
                "remaining": 0,
                "retry_after": retry_after,
            },
            status=429
        )

    # Store current request
    RequestLog.objects.create(
        ip_address=ip
    )

    remaining = MAX_REQUESTS - request_count - 1

    return JsonResponse(
        {
            "success": True,
            "message": "Request successful",
            "limit": MAX_REQUESTS,
            "remaining": remaining,
        }
    )