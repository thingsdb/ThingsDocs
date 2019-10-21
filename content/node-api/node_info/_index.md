---
title: "node_info"
date: 2019-10-14T09:42:49+02:00
weight: 2
---

Returns information about the connected node.

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
libqpack_version | QPack data protocol library version.
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
Information as a `qpack` type bout the connected node.

> This code returns info for the connected node:

```thingsdb
node_info();
```

> Example return value in JSON format

```json
{
    "archive_files": 2,
    "archived_in_memory": 0,
    "cached_names": 3,
    "client_port": 9200,
    "db_stored_event_id": 1,
    "events_in_queue": 0,
    "global_committed_event_id": 11,
    "global_stored_event_id": 11,
    "hostname": "localhost",
    "ip_support": "ALL",
    "libcleri_version": "0.10.1",
    "libpcre2_version": "10.31",
    "libqpack_version": "0.11.0",
    "libuv_version": "1.18.0",
    "local_committed_event_id": 11,
    "local_stored_event_id": 11,
    "log_level": "WARNING",
    "next_event_id": 12,
    "next_thing_id": 8,
    "node_id": 0,
    "node_port": 9220,
    "status": "READY",
    "storage_path": "/var/lib/thingsdb/",
    "syntax_version": "v0",
    "uptime": 15.749372482299805,
    "version": "0.1.5",
    "zone": 0
}
```
