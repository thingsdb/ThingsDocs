---
title: "del"
date: 2019-10-23T16:58:06+02:00
weight: 2
---

Deletes a property from an existing [Type](../../../data-types/type).

### Action

`mod_type(type_name, 'del', property_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | Name of the Type where the property has to be removed from.
del | str | Passing this argument will result in a *Delete* action.
property_name | str | Name of the property that has to be removed.

### Return value

The value `nil`.

> This code shows the return value for the action ***del***:

```thingsdb,json_response
new_type('Person');
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});
mod_type('Person', 'del', 'hobbies');
```

> Return value in JSON format

```json
null
```
