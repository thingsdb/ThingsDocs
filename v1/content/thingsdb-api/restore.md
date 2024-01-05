---
title: "restore"
weight: 344
---

Restore from a backup file created with the [new_backup](#../../node-api/new_backup) function.

Before using this function the following list of requirements must be must be fulfilled:

 - The user performing the restore must have `FULL` privileges on the`@thingsdb` [scope](../../overview/scopes).
 - No collections may exists. Use [collections_info()](../collections_info) and [del_collection(..)](../del_collection) to check and remove existing collections.
 - No modules may exists. Use [modules_info()](../modules_info) and [del_module(..)](../del_module) to check and remove existing modules.
 - No tasks may exists in the `@thingsdb` scope. Use [tasks()](../../collection-api/tasks) and [task(..).del()](../../data-types/task/del) to check and remove existing tasks.
 - All nodes must be *online* and *ready*. If this is *not* the case, then either remove the node or wait for the node to become *ready*. Use [nodes_info()](../../node-api/nodes_info) to check for the status of the nodes.
 - When having *multiple nodes*, all committed changes must be stored as well. Function [nodes_info()](../../node-api/nodes_info) shows both the `committed_change_id` and `stored_change_id` for all nodes. This is *not* a requirement when using a single node.

{{% notice warning %}}
After running this function, **all existing users and tokens will be overwritten**, including the user performing the restore *unless* the `take_access` argument will be set to `true`. In both cases it is required to re-authenticate to ThingsDB after the restore is completed.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`restore(filename, [options])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`filename` | str | Tar file containing the backup, usually a file ending with `.tar.gz`.
`options` | thing (optional) | A thing with optional [options](#options).


#### Options

Option | Type | Description
-------- | ---- | -----------
`take_access` | bool | When `true`, the users and tokens will **not** be restored and all associated *tasks* will be cleared. The user performing the restore will be granted full access to all scopes. Default is `false`.
`restore_tasks` | bool | When `true`, the tasks will be also be restored. If `false` or when `take_access` is set to `true`, all the *tasks* will be cleared. Default is `false`.

{{% notice warning %}}
The options `take_access` and `restore_tasks` cannot both be set to `true`.
{{% /notice %}}

### Return value

Returns `nil` when successful.

### Example

> Restore from a backup file

```thingsdb,syntax_only,@t
restore('/tmp/backup.tar.gz', {
    take_access: true,
    restore_tasks: false,
});
```

> Return value in JSON format

```json
null
```
