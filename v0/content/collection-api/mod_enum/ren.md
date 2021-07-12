---
title: "ren"
weight: 203
---

Rename a member value from an existing [enumerator type](../../../data-types/enum).


### Action

`mod_enum(enum, 'ren', name, to)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | Name of the [enumerator type](../../../data-types/enum) where the member has to be removed from.
`'ren'` | str | Passing this argument will result in a *rename* action.
name | str | Name of the member that has to be modified.
to | str | New name for the member that has to be modified.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***ren***:

```thingsdb,json_response
// Create enum `Color`
set_enum('Color', {
    RED: '#ff0000',
    BLUE: '#00ff00',
    GRAS: '#0000ff',
});

// Modify `GRAS` to `GREEN`
mod_enum('Color', 'ren', 'GRAS', 'GREEN');
```

> Return value in JSON format

```json
null
```
