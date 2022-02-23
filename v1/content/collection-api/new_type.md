---
title: "new_type"
weight: 248
---

Creates a new [Type](../../overview/type). This function *only* creates a new type
and does not allow you to specify any fields. With the [set_type()](../set_type) function
you can define the fields for the new type.

{{% notice note %}}
It is possible to use `set_type` directly without calling `new_type` first. However, sometimes
you want to cross reference two types so you want both type to exists before calling `set_type`.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`new_type(type, [wrap_only])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | string | Name of the Type to be created.
wrap_only | bool (optional) | When `true` the new type will be created with *wrap-only* mode enabled. Default is `false`.

{{% notice note %}}
If **wrap-only** mode is enabled, no typed thing of this type can be
created nor can the type be used by other type. In **wrap-only** mode the only purpose of the type is to [wrap](../../data-types/thing/wrap) other things.
{{% /notice %}}

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
