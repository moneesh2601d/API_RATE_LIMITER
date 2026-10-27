from django.contrib import admin

# Register your models here.
from .models import RequestLog


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):

    list_display = (
        "ip_address",
        "timestamp",
    )

    list_filter = (
        "timestamp",
    )

    search_fields = (
        "ip_address",
    )