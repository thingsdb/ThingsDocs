---
title: "is_nan"
weight: 244
---

This function determines whether the provided value is not a number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_nan(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is not a number, else `false`.

### Example

> This code shows some return values for ***is_nan()***:

```thingsdb,json_response
[
    is_nan( true ),
    is_nan( 123 ),
    is_nan( 3.14 ),
    is_nan( inf ),
    is_nan( [] ),
    is_nan( {} ),
    is_nan( nan ),
    is_nan( '123' ),
];
```

> Return value in JSON format

```json
[
    false,
    false,
    false,
    false,
    true,
    true,
    true,
    true
]
```
