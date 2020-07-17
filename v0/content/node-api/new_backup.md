---
title: "new_backup"
weight: 190
---

Schedule a new backup.

Backups are created using `tar` and `gzip`. Once a backup is made, the `.tar.gz` backup
file can be used to recover ThingsDB, or can be used to load the ThingsDB into another node.
The result value is a backup ID. This ID can be used by [backup_info(..)](../backup_info) for details
about the backup schedule job, or can be used to [delete](../del_backup) the backup schedule.

{{% notice tip %}}
If Google Cloud Storage is [configured](../../getting-started/configuration) then it is possible to create backups directly into Google Cloud Storage.
To use Google Cloud Storage simply create the backup with a `file_template` argument like `gs://my_bucket/my_backup_{DATE}{TIME}.tar.gz`.
{{% /notice %}}

Restoring from a backup file can be done with either the [restore(..)](../../thingsdb-api/restore) function or by starting the node from a backup file. See the [example recovery](#example-recovery) section below on how to start a node from a backup file.

{{% notice note %}}
Before **v0.9.5** it was not possible to schedule a backup when having just a single node. The underlying reason for this restriction used to be that a single node will not enter `away` mode which is required for creating a backup. A scheduled backup is now the exception for a single to enter `away` mode.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`new_backup(file_template, [start_ts, [repeat, [max_files]]]);`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
`file_template` | str | Backup schedule file template. See [file-template](#file-template) for more information.
`start_ts` | nil/int/float/raw (optional) | Start date/time of the backup. If no `start_ts` is given, the backup starts as soon as possible.
`repeat` | int (optional) | Repeat the backup schedule every `repeat` seconds. If no `repeat` value is set, the backup job will run only once.
`max_files` | int (optional) | As soon as `max_files` successful backups are created, the first backup (including the file on disk) will be removed. Default is `7`.

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
// Create a new backup immediately, then at 23:00 and then repeat each day
new_backup('/var/backup/thingsdb_{DATE}{TIME}.tar.gz', '2000-01-01 23:00', 24*3600);
```

> Example result in JSON format:

```json
0
```

### Example recovery

There are two options to restore data from a ThingsDB backup file. One option is to use the [restore(..)](../../thingsdb-api/restore) function
and the other option is explained in the steps below:

```bash
# Unpack a backup file in some storage directory.
tar -xzf backup.tar.gz
```

```bash
# Start ThingsDB with the current path as storage path
THINGSDB_STORAGE_PATH=./ thingsdb --forget-nodes
```

> Confirm with `yes` so we can start with a single node

```none
Warning: all nodes information will be lost!!

Type `yes` + ENTER if you really want to continue: yes
```

Done!
