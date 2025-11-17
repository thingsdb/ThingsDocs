---
title: "rename_type"
weight: 312
---

Rename a [type](../../overview/type).

This function generates a [change](../../overview/changes) and requires a call to [commit()](../commit) if [commit history](../../thingsdb-api/set_history) is enabled for the scope.

### Function

`rename_type(current_name, new_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`current_name` | str (required) | Current [type](../../overview/type) name.
`new_name` | str (required) | New name for the [type](../../overview/type).

### Return value

Returns `nil` when successful.
