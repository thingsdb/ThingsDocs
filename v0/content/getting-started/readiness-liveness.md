---
title: "Readiness and liveness"
weight: 5
chapter: false
---

When `http_status_port` in the configuration file or the environment variable `THINGSDB_HTTP_STATUS_PORT` is set then `/status`, `/ready` and `/healthy` are available.
These can be used for readiness and liveness requests.
