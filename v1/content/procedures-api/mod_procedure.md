---
title: "mod_procedure"
weight: 377
---

Changes the closure for an existing procedure. This function also updates the `created_at` time as if it is a new procedure.

This function generates a [change](../../overview/changes).

### Function

`mod_procedure(name, closure)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`name` | str (required) | Name of the procedure to modify.
`closure` | closure (required) | Closure which will be attached to the procedure.

### Return value

The value `nil`. A [lookup_err()](../../errors/lookup_err) is raised if the procedure does not exist.

### Example

> Create and modify a procedure `add_one`:

```thingsdb,json_response
// Create a new procedure `add_one`
new_procedure('add_one', |x| {
    x + 1;
});

// Modify the procedure to add a doc string
mod_procedure('add_one', |x| {
    "Adds one to a given value";
    x + 1;
});
```

> Return value in JSON format

```json
null
```

