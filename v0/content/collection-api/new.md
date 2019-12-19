---
title: "new"
weight: 122
---

Creates a new instance of a defined [Type](../../data-types/type).

{{% notice info %}}
When possible it is preferred to use the syntax `MyType{...}` to create a instance of a certain type. However, sometimes you need to create an instance dynamically with the type name as variable and then `new()` can be used.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`new(type_name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | The name of the Type that an instance must be made of.
value | thing | Thing containing all the properties to be added to the new instance of the given Type.

### Return value

A Thing containing all the properties which have been added to the new instance of the given Type.

### Example

> This code shows how to use ***new()***:

```thingsdb,json_response
type_name = 'Person';

// Create type `Person`
set_type(type_name, {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});

// Create an instance of type `Person`
new(type_name, {
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
