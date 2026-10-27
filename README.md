# 🚦 API Rate Limiter

> 🛡️ **Control traffic. Prevent abuse. Keep APIs reliable.**

A lightweight **API Rate Limiter** built with **Python, Django, SQLite, HTML, CSS, and JavaScript** to control incoming requests and protect APIs from excessive traffic.

## ✨ Key Features

- 🚥 **Smart Request Limiting** — Restricts the number of requests a client can make within a defined time window.
- 📊 **Request Tracking** — Monitors incoming requests and their timestamps.
- ⚡ **Request Validation** — Determines whether a request should be accepted or rejected.
- 🚫 **HTTP 429 Handling** — Returns `429 Too Many Requests` when the rate limit is exceeded.
- 🖥️ **Interactive Web Interface** — Provides a simple interface to test rate-limiting behavior.
- 🗄️ **SQLite Integration** — Supports database storage for application data.
- 🔧 **Django-Powered Backend** — Handles request processing and rate-limiting logic.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| 🌐 **Django** | Backend framework |
| 🎨 **HTML, CSS & JavaScript** | Frontend interface |
| 🗄️ **SQLite** | Database |
| 💻 **Git & GitHub** | Version control |

## ⚙️ How It Works

🔄 **The request lifecycle:**

1. 📩 **Incoming Request** — A client sends a request to the API.
2. 🆔 **Client Identification** — The rate limiter identifies the client.
3. 🔍 **Limit Check** — The system checks the number of requests within the configured time window.
4. ✅ **Request Allowed** — If the client is within the limit, the request proceeds.
5. 🚫 **Request Blocked** — If the limit is exceeded, the server returns `429 Too Many Requests`.
6. 🔁 **Tracking Updated** — Request information is updated for subsequent checks.
