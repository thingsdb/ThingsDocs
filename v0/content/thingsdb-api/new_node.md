---
title: "new_node"
weight: 168
---

Adds a new node to ThingsDB. Nodes are used for scaling and high availability.

This function generates an [event](../../overview/events).

### Function
`new_node(secret, ip_address [, port]);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`secret` | str (required) | Secret used to initially connect to the new node.
`ip_address` | str (required) | IP Address (IPv4 or IPv6) of the new node.
`port` | int (optional) | Node port (`listen_node_port`), an integer between 0 an 65535, default **9220**.


### Return value

Returns the new node `id` if successful.

### Example

> Add a new node to ThingsDB:

```thingsdb,syntax_only,@t
// ThingsDB must be started on node2 using the `--secret ...` argument
new_node('my-one-time-serect', 'node2.local');
```

> Example return value in JSON format (the new node id)

```json
1
```
