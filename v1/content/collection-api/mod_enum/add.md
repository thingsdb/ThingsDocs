---
title: "add"
weight: 281
---

Adds a member or method to an existing [enumerator type](../../../data-types/enum).


### Action

`mod_enum(enum, 'add', name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | Name of the [enumerator type](../../../data-types/enum) where the member has to be added to.
`'add'` | str | Passing this argument will result in an *add* action.
name | str | Name of the member or method that has to be added.
value | depends | Value of the member that has to be added. The type of the member must be equal to the other enum values. For a method the value must be a closure.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***add***:

```thingsdb,json_response
// Create enum `Color`
set_enum('Color', {
    RED: '#ff0000',
    GREEN: '#00ff00'
});

// Add `BLUE` to enum `Color`
mod_enum('Color', 'add', 'BLUE', '#0000ff');
```

> Return value in JSON format

```json
null
```
