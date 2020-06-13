---
title: "procedure_doc"
weight: 222
---

Returns the doc string for a given procedure. An *empty* string is returned if the procedure has no doc string.

This function does *not* generate an [event](../../overview/events).

### Function

`procedure_doc(procedure);`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`procedure` | str (required) | Name of the procedure where to return the doc string for.

### Return value

Returns the doc string for a given procedure.

### Example

> Create a new procedure `add_one`:

```thingsdb,json_response
new_procedure('add_one', |x| {
    "Adds one to a given value";
    x + 1;
});

// Return the doc string for procedure `add_one`
procedure_doc('add_one');
```

> Return value in JSON format

```json
"Adds one to a given value"
```
