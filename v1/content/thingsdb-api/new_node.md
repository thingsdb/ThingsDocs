---
title: "new_node"
weight: 353
---

Adds a new node to ThingsDB. Nodes are used for scaling and high availability.

Before using this command, make sure another node is started and waiting for a join. This can be done by starting thingsdb with the `--secret` argument, for example:

```bash
thingsdb --secret "my-one-time-secret"
```

Next, you will see something like this:

```text
Waiting for an invite from a node to join ThingsDB...

You can use the following query to add this node:

    new_node('my-one-time-secret', 'node.local', 9220);
```

Now you can use the [new_node(..)](../new_node) function to add the node to ThingsDB.

This function generates a [change](../../overview/changes).

### Function

`new_node(secret, name [, port])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`secret` | str (required) | Secret used to initially connect to the new node.
`name` | str (required) | Node name (host-name or IP address) of the new node.
`port` | int (optional) | Node port (`listen_node_port`), an integer between 0 an 65535, default **9220**.

{{% notice tip %}}
Best practice is to set the argument "**name**" to the same name as specified by the environment variable **THINGSDB_NODE_NAME** or the **node_name** found in the configuration file (view the chapter on [configuration](../../getting-started/configuration)).
{{% /notice %}}

### Return value

Returns the new node `id` if successful.

### Example

> Add a new node to ThingsDB:

```thingsdb,syntax_only,@t
// ThingsDB must be started on node2 using the `--secret ...` argument
new_node('my-one-time-secret', 'node2.local');
```

> Example return value in JSON format (the new node id)

```json
1
```
