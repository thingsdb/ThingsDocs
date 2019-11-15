---
title: "mod"
date: 2019-10-23T16:58:14+02:00
weight: 300
---

Modifies a property from an exinsting [Type](../../../data-types/type).

{{% notice warning %}}
When modifying a property of a Type, the changed property type can only be less 'strict'. \
So for example, `age: 'int'` can become `age: 'int?'`, but not the other way around.
{{% /notice %}}



### Action

`mod_type(type_name, 'mod', property_name, property_type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | Name of the Type where the property has to be removed from.
`'mod'` | str | Passing this argument will result in a *Modify* action.
property_name | str | Name of the property that has to be removed.
property_type | str | Type of the property that has to be modified.

### Return value

The value `nil`.

> This code shows the return value for the action ***mod***:

```thingsdb,json_response
new_type('Person');
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});
mod_type('Person', 'mod', 'age', 'int?');
```

> Return value in JSON format

```json
null
```

