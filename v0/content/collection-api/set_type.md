---
title: "set_type"
weight: 137
---

Defines the properties of a [Type](../../data-types/type). Function `set_type` works only on a new type. Use `mod_type()` if you want to change an existing type, see [mod_type](../mod_type).

This function generates an [event](../../overview/events).

### Function

`set_type(type_name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | The name of the [Type](../../data-types/type) where the properties have to be set.
value | thing | Thing containing all the properties to be set.

### Return value

The value `nil`.

### Example

> This code shows how to use ***set_type()***:

```thingsdb,json_response
set_type('Person', {
    name: 'str',
    age: 'uint',
    hobbies: '[str]'
});
```

> Return value in JSON format

```json
null
```
