---
title: "del_node"
weight: 309
---

This function can be used to delete a node from ThingsDB.

{{% notice warning %}}
Before deleting a node, the node *must* be offline. As long is the node is *active*, you are not allowed
to delete the node. See [shutdown](../../node-api/shutdown) for shutting down a node by using a query.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`del_node(node_id)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
node_id | int (required) | Id of the node to delete.

### Return value

Returns `nil` when successful.
