---
title: "round"
weight: 276
---

Return a number that will be rounded to the decimal places which are given as input.
If the decimal places to be rounded are not specified, it is considered as 0, and it will round to the nearest integer.

This function does *not* generate a [change](../../../overview/changes).

### Function

`round(number, places)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Number to be rounded.
places   | int (optional)       | Number of digits. `0` is nog given.

### Return value

Returns with a [float](../../../data-types/float) or [int](../../../data-types/int), depending on the number input type.

### Example

> ound()_ function examples:

```thingsdb,json_response
[
    round(MATH_PI, 2),
    round(5.8123),
    round(45634, -3),
]
```

> Return value in JSON format

```json
[
    3.14,
    6.0,
    46000
]
```
