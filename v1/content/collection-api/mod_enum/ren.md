---
title: "ren"
weight: 277
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
    GREEN: '#00ff00',
    SKY: '#0000ff',
});

// Modify `SKY` to `BLUE`
mod_enum('Color', 'ren', 'SKY', 'BLUE');
```

> Return value in JSON format

```json
null
```
