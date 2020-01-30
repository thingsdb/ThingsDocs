---
title: "new_procedure"
weight: 181
---


Creates a new procedure to the `@thingsdb` or a `@collection` scope. The name of the procedure must be unique within the scope.
The given closure will be copied to the procedure, so this is *not* a reference to a given closure.

This function generates an [event](../../overview/events).

### Function

`new_procedure(name, closure);`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`name` | str (required) | Name of the new procedure.
`closure` | closure (required) | Closure which will be attached to the procedure.

### Return value

Returns the name of the new procedure.  A [lookup_err()](../../errors/lookup_err) is raised
if the procedure already exists.

### Example

> Create a new procedure `add_one`:

```thingsdb,json_response
// Create a new procedure `add_one`
new_procedure('add_one', |x| {
    "Adds one to a given value";
    x + 1;
});
```

> Return value in JSON format

```json
"add_one"
```
