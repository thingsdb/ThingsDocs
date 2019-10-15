---
title: "int"
date: 2019-10-14T10:00:14+02:00
weight: 21
---

Returns an [int](../../data-types/integer) from a specified value.
If no value is given, the default integer `0` is returned.

If the specified value was a [float](../../data-types/floating-point) value, then the
new integer value will be rounded towards zero.

If the specified value is of type [raw](../../data-types/string-raw), then the initial characters
of the string are converted until a non-digit character is found.
Initial white space is ignored and the number may start with an optional `+` or `-` sign.

Type [bool](../../data-types/boolean) values are converted to `1` for `true` and `0` for `false`.

This function does *not* generate an [event](../../events).

### Function
`int(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value where to create an integer value for.

### Return value
An integer value. In case the integer value is too large for a 64bit integer,
an `OVERFLOW_ERROR` is raised. Other type than `float`, `raw`, `bool` or `int`
will raise a `BAD_REQUEST`.

> This code shows some return values for ***int()***:

```
[
    int(),
    int(2.718),
    int(-1.9),
    int('365 days'),
    int('0xFF'),
    int(true),
    int(false),
];
```

> Return value in JSON format

```json
[
    0,
    2,
    -1,
    365,
    255,
    1,
    0
]
```
