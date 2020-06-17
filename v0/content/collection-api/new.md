---
title: "new"
weight: 162
---

Creates a new instance of a defined [Type](../../data-types/type).

{{% notice info %}}
When possible it is preferred to use the syntax `MyType{...}` to create a instance of a certain Type. However, sometimes you need to create an instance dynamically with the Type's name as variable and then `new()` can be used.
{{% /notice %}}

{{% notice tip %}}
Since version **v0.9.2** the `value` argument is no longer required. If not given all properties will be set to their default values.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`new(type, [value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | The name of the Type that an instance must be made of.
value | thing (optional) | Thing containing all the properties that must be added to the new instance of the given Type.

### Return value

A Thing containing all the properties which have been added to the new instance of the given Type.

### Example

> This code shows how to use ***new()***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});

// Create an instance of type `Person`
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
