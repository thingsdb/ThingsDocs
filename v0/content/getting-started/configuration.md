---
title: "Configuration"
weight: 3
chapter: false
---

ThingsDB can start with a [configuration file](https://github.com/thingsdb/ThingsDB/blob/master/thingsdb.example.conf) and/or with environment variables. However be aware that the environment variables will overwrite the configuration file settings if both apply to the same setting.

Variable | Default | Description
-------- | ------- | -----------
`THINGSDB_LISTEN_CLIENT_PORT` | `9200` | Listen on this TCP port for client socket connections.
`THINGSDB_BIND_CLIENT_ADDR` | `0.0.0.0` | Bind client connections to this address. This may also be an IPv6 address like `::`.
`THINGSDB_NODE_NAME` | *hostname* | ThingsDB will publish itself to other nodes using this node name.
`THINGSDB_LISTEN_NODE_PORT` | `9210` | Listen on this TCP port for node connections.
`THINGSDB_BIND_NODE_ADDR` | `0.0.0.0` | Bind node connections to this address. This may also be an IPv6 address like `::`.
`THINGSDB_IP_SUPPORT` | `ALL` | Listen to IPv4 (`IPV4ONLY`), IPv6 (`IPV6ONLY`) or both (`ALL`) addresses.
`THINGSDB_STORAGE_PATH` | *depends* | Location to store ThingsDB data. The default location depends on the user who is running ThingsDB. (`/var/lib/thingsdb/` for *root* and `~/.thingsdb/` for a normal user).
`THINGSDB_PIPE_CLIENT_NAME` | *disabled* | Named PIPE for client connections. Support for client PIPE connections will be disabled if the value is not configured.
`THINGSDB_THRESHOLD_FULL_STORAGE` | `1000` | Threshold for number of events before initiating a full database store.
`THINGSDB_HTTP_STATUS_PORT` | *disabled* | TCP port for listening to health and readiness checks.
`THINGSDB_HTTP_API_PORT` | *disabled* | TCP port for listening to HTTP API calls.
`THINGSDB_ZONE` | `0` | Start node in this [zone](../../overview/dictionary) number. Zones are used for forwarding queries while in *away* mode.
`THINGSDB_QUERY_DURATION_WARN` | *disabled* | Log a warning message when a query takes more than X second(s).
`THINGSDB_QUERY_DURATION_ERROR` | *disabled* | Log an error message when a query takes more than X second(s).
