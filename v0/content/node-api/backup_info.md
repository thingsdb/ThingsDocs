---
title: "backup_info"
weight: 150
---


Returns information about a specific scheduled backup.

Value | Description
------- | -----------
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the backup schedule is created.
`file_template` | Backup [file template](../new_backup#file-template).
`id` | Backup ID.
`next_run` | Only available when the backup job is scheduled to run. Contains a [string](../../data-types/str) with date/time for the next planned schedule, or *pending* when the backup is scheduled to start.
`repeat` | Only available when the backup will repeat. Contains an [integer](../../data-types/int) value representing the repeat time in seconds.
`result_code` | Only available if the backup job has started at least once. Contains the last result code. (`0` when successful)
`result_message` | Only available if the backup job has started at least once. Contains the last result message.

This function does *not* generate an [event](../../overview/events).

### Function

`backup_info(ID);`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
`ID` | int | ID of the backup schedule to return info for.

### Return value


### Example

>

```thingsdb,syntax_only,@n
// Return backup info of scheduled backup with ID 0:
backup_info(0);
```

> Example result in JSON format:

```json
{
    "created_at": 1579175900,
    "file_template": "/var/backup/thingsdb_{DATE}{TIME}.tar.gz",
    "id": 0,
    "next_run": "2019-12-10 23:00:00Z",
    "repeat": 86400,
    "result_code": 0,
    "result_message": "success - 2019-12-09 23:01:13Z"
}
```