---
title: "set_type"
date: 2019-10-23T16:59:02+02:00
weight: 34
---

Defines the properties of a Type. Function `set_type` works only on a new type. Use `mod_type()` if you want to change an existing type, see [mod_type](../mod_type).

This function generates an [event](../../events).

### Function

`set_type(type_name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | The name of the Type where the properties have to be set.
value | thing | Thing containing all the properities to be set.

### Return value

The value `nil`.

> This code shows how to use ***set_type()***:

```thingsdb,json_response
new_type('Person');
set_type('Person', {
    name: 'str',
    age: 'int',
    hobbies: '[str]'
});
```

> Return value in JSON format

```json
null
```
