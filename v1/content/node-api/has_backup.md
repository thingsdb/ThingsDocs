---
title: "has_backup"
weight: 323
---

Determines if a backup exists in ThingsDB.

This function does *not* generate a [change](../../overview/changes).

### Function

`has_backup(Id)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
Id | int (required) | Backup Id to check.

### Return value

Returns `true` if a backup with a given Id exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_backup()***:

```thingsdb,json_response,@n
has_backup(123);
```

> Return value in JSON format

```json
false
```
