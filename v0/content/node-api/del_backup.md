---
title: "del_backup"
weight: 163
---


Delete a scheduled backup. If the scheduled backup was *pending*, the backup job will be cancelled.

{{% notice warning %}}
Files associated with the backup will **not** be removed. Only the schedule will be deleted.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`del_backup(ID);`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
`ID` | int | Backup ID to delete.

### Return value

Returns `nil`.
