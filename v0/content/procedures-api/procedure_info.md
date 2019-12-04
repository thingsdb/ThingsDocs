---
title: "procedure_info"
weight: 171
---

Returns information about a procedure.

Value | Description
------- | -----------
arguments | Array with positional argument names.
definition | Closure definition.
doc | Doc string of the closure in the procedure.
name | Name of the procedure.
with_side_effects | Boolean value which indicates if this procedure has side effects.

This function does *not* generate an [event](../../overview/events).

### Function

`procedure_info(procedure);`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`procedure` | str (required) | Name of the procedure where to return the info for.

### Return value

Returns [info](../../data-types/info) about a given procedure.

### Example

> Create a new procedure `add_one`:

```thingsdb,json_response
new_procedure('add_one', |x| {
    "Adds one to a given value";
    x + 1;
});

// Return the doc string for procedure `add_one`
procedure_info('add_one');
```

> Return value in JSON format

```json
{
    "arguments": [
        "x"
    ],
    "definition": "|x|{\"Adds one to a given value\";x+1;}",
    "doc": "Adds one to a given value",
    "name": "add_one",
    "with_side_effects": false
}
```
