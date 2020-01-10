---
title: "new_backup"
weight: 148
---

Schedule a new backup.

Backups are created using `tar` and `gzip`. Once a backup is made, the `.tar.gz` backup
file can be used to recover ThingsDB, or can be used to load the ThingsDB into another node.
The result value is a backup ID. This ID can be used by [backup_info(..)](../backup_info) for details
about the backup schedule job, or can be used to [delete](../del_backup) the backup schedule.

See the [example recovery](#example-recovery) section below on how to recover from a backup file.


{{% notice note %}}
At least **two nodes** are required to create a new backup schedule. This is required because ThingsDB needs to enter *away* mode to actually create the backup and this happens only with two or more nodes.
{{% /notice %}}


This function does *not* generate an [event](../../overview/events).

### Function

`new_backup(file_template, [start_ts, [repeat]]);`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
`file_template` | str | Backup schedule file template. See [file-template](#file-template) for more information.
`start_ts` | nil/int/float/raw (optional) | Start date/time of the backup. If no `start_ts` is given, the backup starts as soon as possible.
`repeat` | int (optional) | Repeat the backup schedule every `repeat` seconds. If not `repeat` value is set, the backup job will run only once.

### File template

Backup file templates should end with `.tar.gz`. They may contain some template variable
for creating unique file names.

Variable | description
-------- | -----------
`{DATE}` | Current date using format `%Y%m%d`, for example `20191209`.
`{TIME}` | Current time using format `%H%M%S`, for example `165730`.
`{EVENT}` | Last committed event ID, for example `123456`.

An example file-name could be `/tmp/backup_{EVENT}.tar.gz`.

### Return value

Returns the backup `ID` for the scheduled backup.

### Example

> Use *new_backup* to schedule a ThingsDB backup:

```thingsdb,syntax_only,@n
// Create a new backup immediately, and then at 23:00 and then repeat each day
new_backup('/var/backup/thingsdb_{DATE}{TIME}.tar.gz', '2000-01-01 23:00', 24*3600);
```

> Example result in JSON format:

```json
0
```

### Example recovery

To start a ThingsDB node data from a backup file, the following steps can be done

```bash
# Unpack a backup file in some storage directory.
tar -xzf backup.tar.gz
```

```bash
# Start ThingsDB with the current path as storage path
THINGSDB_STORAGE_PATH=./ thingsdb --forget-nodes
```

> Confirm with `yes` so we can start with a single node

```
Warning: all nodes information will be lost!!

Type `yes` + ENTER if you really want to continue: yes
```

Done!