---
title: "is_thing"
weight: 260
---

This function determines whether the provided value is a [thing](../../../data-types/thing) or not.

{{% notice note %}}
Typed things are also things, so this function returns `true` for both [typed](../../../overview/type) and [non-typed](../../../data-types/thing) things.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_thing(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a thing, else it returns `false`.

### Example

> This code shows some return values for ***is_thing()***:

```thingsdb,json_response
new_type('A');
[
    is_thing( {} ),
    is_thing( A{} ),
    is_thing( [] ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false
]
```
