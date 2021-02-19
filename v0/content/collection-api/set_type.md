---
title: "set_type"
weight: 215
---

Defines the properties of a [Type](../../data-types/type). Function `set_type` works only on a new Type. Use `mod_type()` if you want to change an existing Type, see [mod_type](../mod_type).

This function generates an [event](../../overview/events).

### Function

`set_type(type, value, [wrap_only])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | The name of the [Type](../../data-types/type) where the properties have to be set.
value | thing | Thing containing all the properties to be set.
wrap_only | bool (optional) | When `true` the type will be configured with *wrap-only* mode enabled. Default is `false` for a new type, or untouched if the type already existed.

{{% notice note %}}
If **wrap-only** mode is enabled, no instances of this type can be
created nor can the type be used by other type unless they also have **wrap-only** mode enabled. In **wrap-only** mode the only purpose of the type is to [wrap](../../data-types/thing/wrap) other things.
{{% /notice %}}

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
