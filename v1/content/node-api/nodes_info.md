---
title: "nodes_info"
weight: 335
---

Returns information about all ThingsDB nodes.

Value | Description
------- | -----------
node_name | A node will publish itself to other nodes using the node name. This can be for example an IP address,  hostname , or a fully qualified domain name (FQDN) of the node.
committed_change_id | Last known committed change Id on the node.
node_id | Id which is assigned to the node.
port | TCP port on which the node is listening for node connections.
status | Current status of the node.
stored_change_id | Last known stored change Id on the node.
syntax_version | Language or syntax version which is running on the node.
zone | [Zone](../../overview/dictionary) number to which the node is assigned.

This function does *not* generate a [change](../../overview/changes).

### Function

`nodes_info()`

### Arguments

None

### Return value

List with node [mpdata](../../data-types/mpdata) about all nodes in ThingsDB.

### Example

> This code returns info about all ThingsDB nodes:

```thingsdb,should_pass,@n
nodes_info();
```

> Example return value in JSON format

```json
[
    {
        "address": "node0.local",
        "committed_change_id": 4,
        "node_id": 0,
        "port": 9220,
        "status": "READY",
        "stored_change_id": 4,
        "stream": null,
        "syntax_version": "v1",
        "zone": 0
    },
    {
        "address": "node1.local",
        "committed_change_id": 4,
        "node_id": 1,
        "port": 9220,
        "status": "READY",
        "stored_change_id": 4,
        "stream": "<node-out:1> 192.168.0.10:9220",
        "syntax_version": "v1",
        "zone": 0
    }
]
```
