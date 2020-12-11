---
title: "backup_info"
weight: 215
---


Returns information about a specific scheduled backup.

Value | Description
------- | -----------
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the backup schedule is created.
`file_template` | Backup [file template](../new_backup#file-template).
`files` | List of successful backup files.
`id` | Backup ID.
`max_files` | Maximum number of backup files to store. The oldest file will be removed once `max_files` is reached.
`next_run` | Only available when the backup job is scheduled to run. Contains a [string](../../data-types/str) with date/time for the next planned schedule, or *pending* when the backup is scheduled to start.
`repeat` | Only available when the backup will repeat. Contains an [integer](../../data-types/int) value representing the repeat time in seconds.
`result_code` | Only available if the backup job has started at least once. Contains the last result code. (`0` when successful)
`result_message` | Only available if the backup job has started at least once. Contains the last result message.

This function does *not* generate an [event](../../overview/events).

### Function

`backup_info(ID)`

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
    "created_at": 1594902231,
    "file_template": "/tmp/backup_{DATE}_{TIME}.tar.gz",
    "files": [
        "/tmp/backup_20200714_230014.tar.gz",
        "/tmp/backup_20200715_230019.tar.gz",
        "/tmp/backup_20200716_230018.tar.gz"
    ],
    "id": 0,
    "max_files": 3,
    "next_run": "2020-07-17 23:00:00Z",
    "repeat": 86400,
    "result_code": 0,
    "result_message": "success - 2020-07-16 23:00:18Z"
}
```
