---
title: "del_procedure"
weight: 321
---

Delete a procedure.

This function generates a [change](../../overview/changes).

### Function

`del_procedure(procedure)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
procedure | str (required) | Procedure name to delete.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the procedure does not exist.

### Example

> This code will delete procedure *add_one*:

```thingsdb,json_response
new_procedure('add_one', |x| {
    "Adds one to a given value";
    x + 1;
});

// Delete procedure `add_one`
del_procedure('add_one');
```

> Return value in JSON format

```json
null
```
