---
title: "del_node"
weight: 174
---

Delete a node from ThingsDB.

{{% notice warning %}}
Before deleting a node, the node *must* be offline. As long is the node is *active*, you are not allowed
to delete the node. See [shutdown](../../node-api/shutdown) for shutting down a node by using a query.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`del_node(node_id);`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
node_id | int (required) | Id of the node to delete.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the node id does not exist.
