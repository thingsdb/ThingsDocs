---
title: "set_type"
weight: 318
---

Defines the properties of a [Type](../../overview/type). Function `set_type` works only on a new Type. Use `mod_type()` if you want to change an existing Type, see [mod_type](../mod_type).

This function generates a [change](../../overview/changes) and requires a call to [commit()](../commit) if [commit history](../../thingsdb-api/set_history) is enabled for the scope.

### Function

`set_type(type, value, [flags])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | The name of the [Type](../../overview/type) where the properties have to be set.
value | thing | Thing containing all the properties to be set.
flags | int (optional) | Flags to be *appended* to the type (see [flags](#flags) for a detailed description).

{{% notice note %}}
If **wrap-only** mode is enabled, no instances of this type can be
created nor can the type be used by other type unless they also have **wrap-only** mode enabled. In **wrap-only** mode the only purpose of the type is to [wrap](../../data-types/thing/wrap) other things.
{{% /notice %}}

### Flags

{{% notice warning %}}
Flags are **additive only**. For example, if a type is created with the `WPO` flag using `new_type('T', WPO)`, and subsequently updated via `set_type('T', {..}, ACA)`, the `ACA` flag will be appended while the existing `WPO` flag remains active.
{{% /notice %}}

Flag        | Description
----------- | -----------
`WPO` _(2)_ | When set, the new type will be created with *wrap-only* mode enabled.
`HID` _(4)_ | When set, the new type will be created with *hide-id* enabled. See ["hid" action on mod_type](../mod_type/hid) for more information.
`IDX` _(8)_ | When set, *auto-index* will be enabled for the new type. See ["idx" action on mod_type](../mod_type/idx) for more information.

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
