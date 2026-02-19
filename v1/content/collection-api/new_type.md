---
title: "new_type"
weight: 302
---

Creates a new [Type](../../overview/type). This function *only* creates a new type
and does not allow you to specify any fields. With the [set_type()](../set_type) function
you can define the fields for the new type.

{{% notice note %}}
It is possible to use `set_type` directly without calling `new_type` first. However, sometimes
you want to cross reference two types so you want both type to exists before calling `set_type`.
{{% /notice %}}

This function generates a [change](../../overview/changes) and requires a call to [commit()](../commit) if [commit history](../../thingsdb-api/set_history) is enabled for the scope.

### Function

`new_type(type, [flags])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | string | Name of the Type to be created.
flags | int (optional) | Flags for the new type (see [flags](#flags) for a detailed description).

{{% notice note %}}
If **wrap-only** mode is enabled, no typed thing of this type can be
created nor can the type be used by other type. In **wrap-only** mode the only purpose of the type is to [wrap](../../data-types/thing/wrap) other things.
{{% /notice %}}

### Flags

Flag        | Description
----------- | -----------
`WPO` _(2)_ | When set, the new type will be created with *wrap-only* mode enabled.
`HID` _(4)_ | When set, the new type will be created with *hide-id* enabled. See ["hid" action on mod_type](../mod_type/hid) for more information.
`IDX` _(8)_ | When set, *auto-index* will be enabled for the new type. See ["idx" action on mod_type](../mod_type/idx) for more information.

### Return value

The name of the newly created Type.

### Example

> This code shows a use case where ***new_type()*** is helpful:

```thingsdb,should_pass
new_type('A');
new_type('B');

set_type('A', {
    b: 'B?'
});

set_type('B', {
    a: 'A?'
});

// Return type information
types_info();
```

> Example return value in JSON format

```json
[
    {
        "created_at": 1594384634,
        "fields": [
            ["b", "B?"]
        ],
        "methods": {},
        "modified_at": 1594384634,
        "name": "A",
        "type_id": 0,
        "wrap_only": false
    },
    {
        "created_at": 1594384634,
        "fields": [
            ["a", "A?"]
        ],
        "methods": {},
        "modified_at": 1594384634,
        "name": "B",
        "type_id": 1,
        "wrap_only": false
    }
]
```
