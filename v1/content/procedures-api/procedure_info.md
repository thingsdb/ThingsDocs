---
title: "procedure_info"
weight: 373
---

Returns information about a procedure.

Value | Description
------- | -----------
`arguments` | Array with positional argument names.
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the procedure is created.
`definition` | Closure definition. *(Only available with `CHANGE` privileges)*
`doc` | Doc string of the closure in the procedure.
`name` | Name of the procedure.
`with_side_effects` | Boolean value which indicates if this procedure has side effects and thus requires a [change](../../overview/changes).

This function does *not* generate a [change](../../overview/changes).

### Function

`procedure_info(procedure)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`procedure` | str (required) | Name of the procedure where to return the info for.

### Return value

Returns [mpdata](../../data-types/mpdata) about a given procedure.

### Example

> Create a new procedure `add_one`:

```thingsdb,should_pass
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
    "created_at": 1579175900,
    "definition": "|x| {\n    \"Adds one to a given value\";\n    x + 1;\n}",
    "doc": "Adds one to a given value",
    "name": "add_one",
    "with_side_effects": false
}
```
