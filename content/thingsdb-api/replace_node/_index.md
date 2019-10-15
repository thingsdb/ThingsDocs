---
title: "replace_node"
date: 2019-10-14T09:51:12+02:00
weight: 15
---

Replace a node in ThingsDB. This can be used if an existing node has a
unrecoverable state, for example a hardware failure. This function requires
a node id as its first argument which can be queried using the [nodes_info()](../../node-api/nodes_info)
function.


This function generates an [event](../../events).

### Function
`replace_node(node_id, secret, ip_address [, port]);`


### Arguments
Argument | Type | Description
-------- | ---- | -----------
`node_id` | int (required) | Node id of the node to replace.
`secret` | raw (required) | Secret used to initially connect to the new node.
`ip_address` | raw (required) | IP Address (IPv4 or IPv6) of the new node.
`port` | int (optional) | Node port (`listen_node_port`), an integer between 0 an 65535, default **9220**.


### Return value
Returns `nil` if successful.

> Replace node with id 1:

```
/* node3.local must be started using the `--secret ...` argument
and the node with id 1 must be turned off */
replace_node(1, 'my-one-time-serect', 'node3.local');
```

> Return value in JSON format

```json
null
```