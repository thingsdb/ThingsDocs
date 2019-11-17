---
title: "add"
weight: 100
---

Adds a property to an existing [Type](../../../data-types/type).

### Action

`mod_type(type_name, 'add', property_name, property_type, initial_value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | Name of the Type where the property has to be added to.
`'add'` | str | Passing this argument will result in a *Add* action.
property_name | str | Name of the property that has to be added.
property_type | str | Type of the property that has to be added.
initial_value | any | The default value to set on existing instances of this Type. Only required if the type has active instances.

### Return value

The value `nil`.

> This code shows the return value for the action ***add***:

```thingsdb,json_response
new_type('Person');
set_type('Person', {
    name: 'str',
    age: 'int'
});
mod_type('Person', 'add', 'hobbies', '[str]', ['football']);
```

> Return value in JSON format

```json
null
```
