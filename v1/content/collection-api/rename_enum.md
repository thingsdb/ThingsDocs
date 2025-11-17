---
title: "rename_enum"
weight: 311
---

Rename an [enum](../../data-types/enum) type.

This function generates a [change](../../overview/changes) and requires a call to [commit()](../commit) if [commit history](../../thingsdb-api/set_history) is enabled for the scope.

### Function

`rename_enum(current_name, new_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`current_name` | str (required) | Current [enum](../../data-types/enum) type name.
`new_name` | str (required) | New name for the [enum](../../data-types/enum) type.

### Return value

Returns `nil` when successful.
