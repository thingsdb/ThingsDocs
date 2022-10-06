---
title: "is_float"
weight: 220
---

This function determines whether the provided value is a [floating point](../../data-types/float) value or not.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_float(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a float, else it returns `false`.

### Example

> This code shows some return values for ***is_float()***:

```thingsdb,json_response
[
    is_float( 42.0 ),
    is_float( 0.42e+2 ),
    is_float( 42 ),
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
