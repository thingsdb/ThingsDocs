---
title: "restore"
weight: 256
---

Restore from a backup file created with the [new_backup](#../../node-api/new_backup) function.

Before using this function the following list of requirements must be must be fulfilled:

 - The user performing the restore must have `FULL` privileges on the`@thingsdb` [scope](../../overview/scopes).
 - No collections may exists. Use [collections_info()](../collections_info) and [del_collection(..)](../del_collection) to remove existing collections.
 - All nodes must be *online* and *ready*. If this is *not* the case, then either remove the node or wait for the node to become *ready*. Use [nodes_info()](../../node-api/nodes_info) to check for the status of the nodes.
 - When having *multiple nodes*, all committed events must be stored as well. Function [nodes_info()](../../node-api/nodes_info) shows both the `committed_event_id` and `stored_event_id` for all nodes. This is *not* a requirement when using a single node.

{{% notice warning %}}
After running this function, **all existing users and tokens will be overwritten**, including the user performing the restore *unless* the `take_access` argument will be set to `true`. In both cases it is required to re-authenticate to ThingsDB after the restore is completed.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`restore(filename, [take_access])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`filename` | str | Tar file containing the backup, usually a file ending with `.tar.gz`.
`take_access` | bool (optional) | When `true`, the users and tokens will **not** be restored, but instead the user performing the restore will be granted full access to all scopes. Default is `false`.


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
