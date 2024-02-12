---
title: "mod"
weight: 274
---

Modify a member value or method closure from an existing [enumerator type](../../../data-types/enum).


### Action

`mod_enum(enum, 'mod', name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | Name of the [enumerator type](../../../data-types/enum) where the member has to be removed from.
`'mod'` | str | Passing this argument will result in a *modify* action.
name | str | Name of the member or method that has to be modified.
value | any | New value for the member or method that has to be modified.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***mod***:

```thingsdb,json_response
// Create enum `Color`
set_enum('Color', {
    RED: '#ff0000',
    GREEN: '#00ff00',
    BLUE: '#0000aa',
});

// Modify the value for `BLUE`
mod_enum('Color', 'mod', 'BLUE', '#0000ff');
```

> Return value in JSON format

```json
null
```
