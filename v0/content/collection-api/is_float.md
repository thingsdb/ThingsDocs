---
title: "is_float"
weight: 163
---

This function determines whether the provided value is a [floating point](../../data-types/float) value or not.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isfloat` which will be removed in the next *minor* release.
{{% /notice %}}

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
