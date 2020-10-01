---
title: "del_backup"
weight: 198
---


Delete a scheduled backup. If the scheduled backup was *pending*, the backup job will be cancelled.

This function does *not* generate an [event](../../overview/events).

### Function

`del_backup(ID, [delete_files]);`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
`ID` | int | Backup ID to delete.
`delete_files` | bool (optional) | Delete related backup files from disk *(or Google Cloud Storage)*. Default is `false`.

### Return value

Returns `nil`.
