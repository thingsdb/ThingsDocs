---
title: "del_backup"
weight: 281
---


Delete a scheduled backup. If the scheduled backup was *pending*, the backup job will be cancelled.

This function does *not* generate a [change](../../overview/changes).

### Function

`del_backup(Id, [delete_files])`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
`Id` | int | Backup Id to delete.
`delete_files` | bool (optional) | Delete related backup files from disk *(or Google Cloud Storage)*. Default is `false`.

### Return value

Returns `nil`.
