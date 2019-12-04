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

Besides the preferred **token** authentication, the HTTP API has also support for

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
  "node_id": 0,
  "version": "0.2.18+debug",
  "syntax_version": "v0",
  "msgpack_version": "3.2.0",
  "libcleri_version": "0.12.0",
  "libuv_version": "1.30.1",
  "libpcre2_version": "10.32",
  "status": "READY",
  "zone": 0,
  "log_level": "DEBUG",
  "hostname": "xjoente",
  "client_port": 9200,
  "node_port": 9220,
  "ip_support": "ALL",
  "storage_path": "/home/joente/workspace/thingsdb/itest/testdir/tdb0/",
  "uptime": 9468.000403818,
  "events_in_queue": 0,
  "archived_in_memory": 26,
  "archive_files": 0,
  "local_stored_event_id": 12,
  "local_committed_event_id": 38,
  "global_stored_event_id": 12,
  "global_committed_event_id": 38,
  "db_stored_event_id": 12,
  "next_event_id": 39,
  "next_thing_id": 5,
  "cached_names": 3,
  "http_status_port": "disabled",
  "http_api_port": 9210,
  "scheduled_backups": 0,
  "yajl_version": "2.1.0"
}
```
