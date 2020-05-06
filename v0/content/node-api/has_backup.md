---
title: "has_backup"
weight: 164
---

Determines if a backup exists in ThingsDB.

This function does *not* generate an [event](../../overview/events).

### Function

`has_backup(ID)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
ID | int (required) | Backup ID to check.

### Return value

Returns `true` if a backup with a given ID exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_backup()***:

```thingsdb,json_response,@n
has_backup(123);
```

> Return value in JSON format

```json
false
```
