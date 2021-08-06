---
title: "mod"
weight: 203
---

Modify a member value from an existing [enumerator type](../../../data-types/enum).


### Action

`mod_enum(enum, 'mod', name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | Name of the [enumerator type](../../../data-types/enum) where the member has to be removed from.
`'mod'` | str | Passing this argument will result in a *modify* action.
name | str | Name of the member that has to be modified.
value | any | New value for the member that has to be modified.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***mod***:

```thingsdb,json_response
// Create enum `Color`
set_enum('Color', {
    RED: '#ff0000',
    BLUE: '#00ff00',
    GREEN: '#0000aa',
});

// Modify the value for `GREEN`
mod_enum('Color', 'mod', 'GREEN', '#0000ff');
```

> Return value in JSON format

```json
null
```