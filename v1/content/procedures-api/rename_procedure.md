---
title: "rename_procedure"
weight: 395
---

Rename a procedure.

This function generates a [change](../../overview/changes) and requires a call to [commit()](../../collection-api/commit) if [commit history](../../thingsdb-api/set_history) is enabled for the scope.

### Function

`rename_procedure(current_name, new_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`current_name` | str (required) | Current procedure name.
`new_name` | str (required) | New name for the procedure.

### Return value

Returns `nil` when successful.
