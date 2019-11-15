---
title: "new"
date: 2019-10-23T16:58:40+02:00
weight: 2700
---

Creates a new instance of a defined [Type](../../data-types/type).

This function generates an [event](../../events).

### Function

`new(type_name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | The name of the Type that an instance must be made of.
value | thing | Thing containing all the properities to be added to the new instance of the given Type.

### Return value

A Thing containing all the properities which have been added to the new instance of the given Type.

> This code shows how to use ***new()***:

```thingsdb,json_response
new_type('Person');
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});
new('Person', {
    name: 'John',
    age: 34,
    hobbies: ['Football']
});
```

> Return value in JSON format

```json
{
    "name": "John",
    "age": 34,
    "hobbies": ["Football"]
}
```

{{% notice note %}}
The property names and (data) types of the values that are added to an instance of an existing type must exactly match that Type.
{{% /notice %}}
