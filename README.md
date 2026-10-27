# API_RATE_LIMITER
A lightweight API Rate Limiter built using Django, Python, SQLite, HTML, CSS, and JavaScript. This project demonstrates how to control the number of requests a client can make within a specified time window to prevent API abuse and maintain service reliability.

Features

Request Limiting: Restricts the number of API requests allowed within a configurable time window.

Rate Limit Tracking: Tracks incoming requests and their timestamps.

Request Validation: Determines whether incoming requests should be allowed or rejected.

HTTP 429 Response: Returns 429 Too Many Requests when the rate limit is exceeded.

Web Interface: Provides a simple interface to interact with and test the rate limiter.

SQLite Database: Uses SQLite for storing application data where required.

Django Backend: Handles request processing and rate-limiting logic.

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, JavaScript

Database: SQLite

Tools: Git, GitHub, VS Code

How It Works

A client sends a request to the API.

The rate limiter identifies the client.

It checks the number of requests made within the configured time window.

If the client is within the limit, the request is allowed.

If the limit is exceeded, the server rejects the request with an HTTP 429 Too Many Requests response.

Request counts are updated for subsequent requests.
