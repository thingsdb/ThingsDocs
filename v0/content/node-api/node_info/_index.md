---
title: "node_info"
date: 2019-10-14T09:42:49+02:00
weight: 6
---

Returns information about the node in the current scope.
See [scopes](../../scopes) for more information on how to target a specific node scope.

Value | Description
------- | -----------
archive_files | Number of archive files. May decrease after a full store during *away* mode.
archived_in_memory | Number of events which are archived in memory.
cached_names | Number of [names](../../names) cached in memory.
client_port | Listening for client TCP socket connections on this port.
db_stored_event_id | Last stored event ID in full database store.
events_in_queue | Events which are pending in the queue.
global_committed_event_id | Lowest known committed event ID by all nodes.
global_stored_event_id | Lowest known stored event ID by all nodes.
hostname | Hostname of the node.
http_status_port | Listening to this HTTP port for status, readiness and liveness requests.
ip_support | Enabled IP support. May be IPv4/IPv6 or both.
libcleri_version | Cleri language parser library version.
libpcre2_version | PCRE regular expression library version.
msgpack_version | MessagePack data protocol library version.
libuv_version | UV asynchronous library version.
local_committed_event_id | Last committed event ID on the node.
local_stored_event_id | Last stored event ID on disk. Store takes place when in *away* mode.
log_level | Current log level for the node. May be changed at runtime using [set_log_level(..)](../../node-api/set_log_level)
next_event_id | Next free event ID.
next_thing_id | Next free things ID.
node_id | The `id` which is assigned to the node.
node_port | Listening for node TCP socket connections on this port.
status | Current status of the ThingsDB node.
storage_path | Path used for storing ThingsDB data.
syntax_version | Language or syntax version. A new version of ThingsDB might also have a new language version.
uptime | Uptime of the node in seconds.
version | Version of ThingsDB,
zone | Zone number to which the node is assigned. May be changed in the ThingsDB configuration file.

This function does *not* generate an [event](../../events).

### Function
`node_info()`

### Arguments
None

### Return value
Information as a `msgpack` type bout the connected node.

> This code returns info for the connected node:

```thingsdb,should_pass,@n
node_info();
```

> Example return value in JSON format

```json
{
    "archive_files": 1,
    "archived_in_memory": 0,
    "cached_names": 2,
    "client_port": 9200,
    "db_stored_event_id": 1,
    "events_in_queue": 0,
    "global_committed_event_id": 2,
    "global_stored_event_id": 2,
    "hostname": "node.things",
    "http_status_port": "disabled",
    "ip_support": "ALL",
    "libcleri_version": "0.11.0",
    "libpcre2_version": "10.32",
    "libuv_version": "1.24.1",
    "local_committed_event_id": 2,
    "local_stored_event_id": 2,
    "log_level": "WARNING",
    "msgpack_version": "3.2.0",
    "next_event_id": 3,
    "next_thing_id": 5,
    "node_id": 0,
    "node_port": 9220,
    "scheduled_backups": 0,
    "status": "READY",
    "storage_path": "/var/lib/thingsdb/",
    "syntax_version": "v0",
    "uptime": 7.854678630828857,
    "version": "0.2.7",
    "zone": 0
}
```
