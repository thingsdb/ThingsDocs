---
title: "is_tel"
weight: 239
---

This function determines whether the provided value is of
type [str](../../../data-types/str) and contains a telephone number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_tel(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str` and contains a telephone number, else `false`.

### Example

> This code shows some return values for ***is_tel()***:

```thingsdb,json_response
[
    is_tel( '+31 012345678' ),
    is_tel( '380-44-123-4567' ),
    is_tel( '(011) 380 44 123 4567' ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    true
]
```
