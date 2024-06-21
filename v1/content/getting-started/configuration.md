---
title: "Configuration"
weight: 5
chapter: false
---

ThingsDB can start with a [configuration file](https://github.com/thingsdb/ThingsDB/blob/main/thingsdb.example.conf) and/or with environment variables. However be aware that the environment variables will overwrite the configuration file settings if both apply to the same setting.

Variable | Default | Description
-------- | ------- | -----------
`THINGSDB_BIND_CLIENT_ADDR` | `127.0.0.1` | Bind client connections to this address. This variable both allows an IPv4 address like `0.0.0.0` or IPv6 like `::`.
`THINGSDB_BIND_NODE_ADDR` | `127.0.0.1` | Bind node connections to this address. This variable both allows an IPv4 address like `0.0.0.0` or IPv6 like `::`.
`THINGSDB_CACHE_EXPIRATION_TIME` | `900` | Cached queries which are not used within this expiration time *(in seconds)* will be removed from the cache while the node is in *away* mode. A value of `0` will disable the query cache.
`THINGSDB_GCLOUD_KEY_FILE` | *disabled* | Service Authentication file *(e.g service_account.json)* used for creating backups in Google Cloud Storage. Support for Google Cloud Storage will be disabled if the value is not configured. Note that `gcloud` and `gsutil` must be installed to use this service.
`THINGSDB_HTTP_API_PORT` | *disabled* | TCP port for listening to HTTP API calls _(`9210` is commonly used when enabled)_.
`THINGSDB_HTTP_STATUS_PORT` | *disabled* | TCP port for listening to health and readiness checks _(`8080` is commonly used when enabled)_..
`THINGSDB_IP_SUPPORT` | `ALL` | Listen to IPv4 (`IPV4ONLY`), IPv6 (`IPV6ONLY`) or both (`ALL`) addresses.
`THINGSDB_LISTEN_CLIENT_PORT` | `9200` | Listen to this TCP port for client socket connections.
`THINGSDB_LISTEN_NODE_PORT` | `9220` | Listen to this TCP port for node connections.
`THINGSDB_MODULES_PATH` | *depends* | Path where ThingsDB modules are stored. The default location depends on the user who is running ThingsDB. (`/usr/lib/thingsdb-modules` for *root* and `~/.thingsdb-modules/` for a normal user).
`THINGSDB_NODE_NAME` | *hostname* | ThingsDB will publish itself to other nodes using this node name.
`THINGSDB_PIPE_CLIENT_NAME` | *disabled* | Named PIPE for client connections. Support for client PIPE connections will be disabled if the value is not configured.
`THINGSDB_PYTHON_INTERPRETER` | `python` | Interpreter used for running `*.py` module files *(may also be set to an absolute path like `/usr/bin/python`)*. An *informational message* will be logged if the Python interpreter is not found when starting ThingsDB.
`THINGSDB_QUERY_DURATION_ERROR` | *disabled* | Log an error message when a query takes more than X second(s) *(accepts a floating point value like `1.5`)*.
`THINGSDB_QUERY_DURATION_WARN` | *disabled* | Log a warning message when a query takes more than X second(s) *(accepts a floating point value like `1.5`)*.
`THINGSDB_RESULT_SIZE_LIMIT` | `20971520` *(20 MiB)* | Result size limit is checked when packing properties for a thing. If, at the check moment, the packed data size exceeds the limit, packing stops and an [RESULT_TOO_LARGE](../../errors/#internal-errors) error will be returned. This limit is set in bytes and is used to prevent a huge amount of data, typically when a high `deep` value is used.
`THINGSDB_SHUTDOWN_PERIOD` | `6` | Period in seconds before shutting down. This window provides clients to re-connect to another node. _Note: the shutdown period value is only used when having multiple nodes._
`THINGSDB_STORAGE_PATH` | *depends* | Location to store ThingsDB data. The default location depends on the user who is running ThingsDB. (`/var/lib/thingsdb/` for *root* and `~/.thingsdb/` for a normal user).
`THINGSDB_THRESHOLD_FULL_STORAGE` | `1000` | Threshold for number of events before initiating a full database store.
`THINGSDB_THRESHOLD_QUERY_CACHE` | `160` | Queries with a length equal to, or greater than this threshold will be cached by the node.
`THINGSDB_WS_PORT` | *disabled* | [WebSocket](../../connect/websocket/) port  _(`9270` is commonly used when enabled)_.
`THINGSDB_WS_KEY_FILE` | *none* | Path to private key file _(required for [Secure WebSockets](../../connect/websocket/#secure-websockets))_.
`THINGSDB_WS_CERT_FILE` | *none* | Path to certificate file _(required for [Secure WebSockets](../../connect/websocket/#secure-websockets))_.
`THINGSDB_ZONE` | `0` | Start node in this [zone](../../overview/dictionary) number. Zones are used for forwarding queries while in *away* mode.


Additionally, the environment variable `THINGSDB_INIT`, `THINGSDB_SECRET` and `THINGSDB_DEPLOY` can be used to replace command line arguments which is [documented here](../start-up-node/#flags-as-environment-variable).
