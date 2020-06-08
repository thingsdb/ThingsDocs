---
title: "mod"
weight: 159
---

Modifies the type definition of a property from an existing [Type](../../../data-types/type).

{{% notice note %}}
When modifying a property of a Type, the changed property type can only be less 'strict'. \
So for example, `age: 'int'` can become `age: 'int?'`, but not the other way around.
{{% /notice %}}

### Action

`mod_type(type, 'mod', name, definition)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where the property has to be modified from.
`'mod'` | str | Passing this argument will result in a *modify* action.
name | str | Name of the property that has to be modified.
definition | str | New type definition of the property that has to be modified.

### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***mod***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});

// Make `age` nillable
mod_type('Person', 'mod', 'age', 'int?');
```

> Return value in JSON format

```json
null
```
