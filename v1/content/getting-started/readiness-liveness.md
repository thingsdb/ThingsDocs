---
title: "Readiness and liveness"
weight: 6
chapter: false
---

When `http_status_port` is set in the configuration file or the environment variable `THINGSDB_HTTP_STATUS_PORT` then `/status`, `/ready` and `/healthy` are available.
These can be used for readiness and liveness requests.

### Liveness

The ThingsDB `/healthy` check will respond with a `200 OK` whenever possible and will never respond with an error. So only if _no response_ is received in some reasonable amount of time, the node should be considered as unhealthy.
It is common to use the `/healthy` check as liveness probe in environments like Kubernetes.

### Readiness

Besides the `/healthy` check there is also a `/ready` check. This check responds with `200 OK` if the node has one of the following status: `READY`, `AWAY`, or `AWAY_SOON`. With any other status, for example, `SYNCHRONIZING`, the `/ready` check will respond with `503 Service Unavailable` _(NOK)_.

Since **v0.9.20** ThingsDB will _also_ respond with `200 OK` to a `/ready` request when all of the following conditions are met:

- ThingsDB must be started with the `--deploy` argument.
- The ThingsDB node status is `SYNCHRONIZING`.
- At least one ThingsDB node is unavailable (checked using at least 3 attempts).

{{% notice tip %}}
The following link will explain how to deploy ThingsDB in GKE (Google Kubernetes Engine) and can be used as an example for using the `/ready` and `/healthy` handlers:
[https://github.com/thingsdb/ThingsDB/tree/master/gke#readme](https://github.com/thingsdb/ThingsDB/tree/master/gke#readme)
{{% /notice %}}
