---
title: "new_type"
weight: 118
---

Creates a new [Type](../../data-types/type). This function *only* creates a new type
and does not allow you to specify any fields. With the [set_type()](../set_type) function
you can define the fields for the new type.

{{% notice note %}}
It is possible to use `set_type` directly without calling `new_type` first. However, sometimes
you want to cross reference two types so you want both type to exists before calling `set_type`.
{{% /notice %}}


This function generates an [event](../../overview/events).

### Function

`new_type(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | string | Name of the Type to be created.

### Return value

The name of the newly created Type.

### Example

> This code shows a use case where ***new_type()*** is helpful:

```thingsdb,json_response
type_a = 'A';
type_b = 'B';

new_type(type_a);
new_type(type_b);

set_type(type_a, {
    b: type_b
});

set_type(type_b, {
    a: type_a
});

// Return type information
types_info();
```

> Return value in JSON format

```json
{
    "A": {
        "b": "B"
    },
    "B": {
        "a": "A"
    }
}
```
