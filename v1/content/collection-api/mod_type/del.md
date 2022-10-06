---
title: "del"
weight: 252
---

Deletes a property or method from an existing [Type](../../../overview/type).

{{% notice warning %}}
A property will be removed from all the active instances of that Type.
{{% /notice %}}

### Action

`mod_type(type, 'del', name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where the property has to be removed from.
`'del'` | str | Passing this argument will result in a *delete* action.
name | str | Name of the property or method that has to be removed.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***del***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});

// Delete `hobbies` from type `Person`
mod_type('Person', 'del', 'hobbies');
```

> Return value in JSON format

```json
null
```
