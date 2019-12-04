---
title: "del"
weight: 117
---

Deletes a property from an existing [Type](../../../data-types/type).

{{% notice warning %}}
The property will be removed from all the active instances of that type.
{{% /notice %}}

### Action

`mod_type(type_name, 'del', property_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | Name of the Type where the property has to be removed from.
`'del'` | str | Passing this argument will result in a *delete* action.
property_name | str | Name of the property that has to be removed.

### Return value

The value `nil`.

> This code shows the return value for the action ***del***:

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
