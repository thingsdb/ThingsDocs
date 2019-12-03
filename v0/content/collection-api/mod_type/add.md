---
title: "add"
weight: 111
---

Adds a property to an existing [Type](../../../data-types/type).

{{% notice info %}}
If there are active instances of the type you want to modify, then an *initial_value* is required.
This value is used *only once* for applying the value to the existing instances and is not used when new instances are created.
{{% /notice %}}


### Action

`mod_type(type_name, 'add', property_name, property_type, [initial_value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | Name of the [Type](../../../data-types/type) where the property has to be added to.
`'add'` | str | Passing this argument will result in an *add* action.
property_name | str | Name of the property that has to be added.
property_type | str | Type definition of the property that has to be added.
initial_value | any | The default value to set on existing instances of this [Type](../../../data-types/type).

### Return value

The value `nil`.

> This code shows the return value for the action ***add***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    age: 'int'
});

// Add `hobbies` to type `Person`
mod_type('Person', 'add', 'hobbies', '[str]');
```

> Return value in JSON format

```json
null
```
