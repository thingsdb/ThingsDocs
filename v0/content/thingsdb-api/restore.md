---
title: "restore"
weight: 211
---

Restore from a backup file created with the [new_backup](#../../node-api/new_backup) function.

Before using this function the following list of requirements must be must be fulfilled:

 - The user performing the restore must have `FULL` privileges on the`@thingsdb` [scope](../../overview/scopes).
 - No collections may exists. Use [collections_info()](../collections_info) and [del_collection(..)](../del_collection) to remove existing collections.
 - All nodes must be *online* and *ready*. If this is *not* the case, then either remove the node or wait for the node to become *ready*. Use [nodes_info()](../../node-api/nodes_info) to check for the status of the nodes.
 - When having multiple nodes, all committed events must be stored as well.

{{% notice warning %}}
After running this function, **all existing users and tokens will be overwritten**, including the user performing the *restore*.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`restore(fn);`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`fn` | str | Tar file containing the backup, usually a file ending with `.tar.gz`.

### Return value

Returns `nil` when successful.

### Example

> Restore from a backup file

```thingsdb,syntax_only,@t
restore('/tmp/backup.tar.gz');
```

> Return value in JSON format

```json
null
```
