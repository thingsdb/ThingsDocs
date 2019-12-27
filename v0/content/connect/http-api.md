---
title: "HTTP API"
weight: 4
---


Before using the HTTP API, make sure at least one node has the API port enabled.
By default the API port is enabled and listening to TCP port `9210` but can be disabled or changed
with the `http_api_port` in the [configuration file](https://github.com/thingsdb/ThingsDB/blob/master/thingsdb.example.conf)
or with the `THINGSDB_HTTP_API_PORT` environment variable.

The API has support for both [MessagePack](https://msgpack.org) and [JSON](https://www.json.org) and can be used to perform queries and run procedures.


{{% notice tip %}}
Use **MessagePack** if possible since this is the data serialization protocol which is used by ThingsDB
internally and will therefore be a faster than JSON. It also allows for sending and receiving binary data and is usually more compact than JSON.
In most examples here we use JSON just because it is more readable.
{{% /notice %}}


## Headers

The header field `Content-Type` is required and needs to be either `application/msgpack` or `application/json`.


## Query request

field | description
----- | -----------
`type` | Required and must be `query` for a query request.
`code` | Required string with the query code to preform.
`vars` | Optional and may contain a `map` where the `keys` are variable names and the `values` will be the variable values.

## Query example

> Example using *curl* with *token* authentication:

```bash
curl http://127.0.0.1:9210/thingsdb \
-H "Authorization: TOKEN RzDFlsoucQfDqrwrfGGEtc" \
-H 'Content-Type: application/json' \
-d \
"
{
    \"type\": \"query\",
    \"code\": \"1 + 1;\"
}"
```

> Response

```json
2
```

Besides the preferred **token** authentication, the HTTP API has also support for **basic** authentication.

> Another *curl* example using *basic* authentication:

```bash
curl http://127.0.0.1:9210/node \
--user admin:pass \
-H 'Content-Type: application/json' \
-d \
"
{
    \"type\": \"query\",
    \"code\": \"node_info();\"
}"
```

> Example response:

```json
{
    "archive_files": 1,
    "archived_in_memory": 67,
    "cached_names": 16,
    "client_port": 9200,
    "db_stored_event_id": 1,
    "events_in_queue": 0,
    "global_committed_event_id": 69,
    "global_stored_event_id": 2,
    "hostname": "node",
    "http_api_port": 9210,
    "http_status_port": "disabled",
    "ip_support": "ALL",
    "libcleri_version": "0.12.0",
    "libpcre2_version": "10.32",
    "libuv_version": "1.30.1",
    "local_committed_event_id": 69,
    "local_stored_event_id": 2,
    "log_level": "WARNING",
    "msgpack_version": "3.2.1",
    "next_event_id": 70,
    "next_thing_id": 12,
    "node_id": 0,
    "node_port": 9220,
    "scheduled_backups": 0,
    "status": "READY",
    "storage_path": "/var/lib/thingsdb/",
    "syntax_version": "v0",
    "uptime": 26567.278152959,
    "version": "0.3.5",
    "yajl_version": "2.1.0",
    "zone": 0
}
```
