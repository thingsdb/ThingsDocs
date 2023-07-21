---
title: "is_tuple"
weight: 246
---

This function determines whether the provided value is a [tuple](../../../data-types/tuple) or not. At least nested arrays are of kind tuple.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_tuple(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a tuple, else it returns `false`.

### Example

> This code shows some return values for ***is_tuple()***:

```thingsdb,json_response
[
    is_tuple( [] ),
    is_tuple( tmp = [['nested'], set()] ),
    is_tuple( tmp[0] ),
    is_tuple( tmp[1] ),
];
```

> Return value in JSON format

```json
[
    false,
    false,
    true,
    true
]
```
