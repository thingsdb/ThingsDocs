---
title: "del"
weight: 197
---

Delete a member from an existing [enumerator type](../../../data-types/enum).

{{% notice warning %}}
A member may only be removed if the member is no longer being used. Otherwise an [operation_err()](../../../errors/operation_err) is raised.
{{% /notice %}}

### Action

`mod_enum(enum, 'del', name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | Name of the [enumerator type](../../../data-types/enum) where the member has to be removed from.
`'del'` | str | Passing this argument will result in a *delete* action.
name | str | Name of the member to be removed.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***del***:

```thingsdb,json_response
// Create enum `Color`
set_enum('Color', {
    RED: '#ff0000',
    BLUE: '#00ff00'
});

// Remove `BLUE` from enum `Color`
mod_enum('Color', 'del', 'BLUE');
```

> Return value in JSON format

```json
null
```
