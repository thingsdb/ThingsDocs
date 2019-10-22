---
title: "nodes_info"
date: 2019-10-14T09:43:03+02:00
weight: 3
---

Returns information about all ThingsDB nodes.

Value | Description
------- | -----------
address | IP address or hostname of the node.
committed_event_id | Last known committed event ID on the node.
next_thing_id | Next free thing ID on the node.
node_id | ID which is assigned to the node.
port | TCP port on which the node is listening for node connections.
status | Current status of the node.
stored_event_id | Last known stored event ID on the node.
syntax_version | Language or syntax version which is running on the node.
zone | Zone number to which the node is assigned.


This function does *not* generate an [event](../../events).

### Function
`nodes_info()`

### Arguments
None

### Return value
Array as `msgpack` type containing node information for all nodes within ThingsDB.

> This code returns info for all ThingsDB nodes:

```thingsdb,should_pass,@n
nodes_info();
```

> Example return value in JSON format

```json
[
    {
        "address": "node.things",
        "committed_event_id": 2,
        "next_thing_id": 5,
        "node_id": 0,
        "port": 9220,
        "status": "READY",
        "stored_event_id": 2,
        "stream": null,
        "syntax_version": "v0",
        "zone": 0
    }
]
```
