---
title: "new"
weight: 300
---

Creates a new typed thing of a defined [Type](../../overview/type).

{{% notice info %}}
When possible it is preferred to use the syntax `MyType{...}` to create a thing of a certain Type. However, sometimes you need to create an thing dynamically with the Type's name as variable and then `new()` can be used. {{% /notice %}}

{{% notice tip %}}
Since version **v0.9.2** the `value` argument is no longer required. If not given all properties will be set to their default values.
{{% /notice %}}

{{% notice tip %}}
Since version **v0.9.5** it is also possible to create a typed thing using the shorter syntax `Type(thing)` *(instead of writing `new("Type", thing)`)*.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`new(type, [value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | The name of the Type that a thing must be made of.
value | thing (optional) | Thing containing all the properties that must be added to the new thing of the given Type.

### Return value

A Thing containing all the properties which have been added to the new thing of the given Type.

### Example

> This code shows how to use ***new()***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});

// Create a typed thing of type `Person`
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
The property names and (data) types of the values that are added to a typed thing of an existing type must exactly match that Type.
{{% /notice %}}
