---
title: "add"
weight: 178
---

Adds a member to an existing [enumerator type](../../../data-types/enum).


### Action

`mod_enum(enum, 'add', name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | Name of the [enumerator type](../../../data-types/enum) where the member has to be added to.
`'add'` | str | Passing this argument will result in an *add* action.
name | str | Name of the member that has to be added.
value | depends | Value of the member that has to be added. The type of the member must be equal to the other enum values.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***add***:

```thingsdb,json_response
// Create enum `Color`
set_enum('Color', {
    RED: '#ff0000',
    BLUE: '#00ff00'
});

// Add `GREEN` to enum `Color`
mod_enum('Color', 'add', 'GREEN', '#0000ff');
```

> Return value in JSON format

```json
null
```
