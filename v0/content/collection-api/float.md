---
title: "float"
weight: 121
---

Returns a [float](../../data-types/float) from a specified value.
If no value is given, the default float `0.0` is returned.

If the specified value is of type [str](../../data-types/str), then the initial characters
of the string are converted until a non-digit character is found.
Initial white space is ignored and the number may start with an optional `+` or `-` sign.

Type [bool](../../data-types/bool) values are converted to `1.0` for `true` and `0.0` for `false`.

This function does *not* generate an [event](../../events).

### Function

`float(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value where to create a floating point value for.

### Return value

A floating point value. Other type than `float`, `str`, `bool` or `int`
will raise a `BAD_REQUEST`.

### Example

> This code shows some return values for ***float()***:

```thingsdb,json_response
[
    float(),
    float(42),
    float('0.365e+3 days'),
    float('0xFF'),
    float(true),
    float(false),
];
```

> Return value in JSON format

```json
[
    0,
    42.0,
    365.0,
    255.0,
    1.0,
    0.0
]
```
