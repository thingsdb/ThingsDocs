---
title: "isint"
weight: 119
---

This function determines whether the provided value is an [integer](../../data-types/int) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`isint(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is an integer, else it returns `false`.

### Example

> This code shows some return values for ***isint()***:

```thingsdb,json_response
[
    isint( 42 ),
    isint( 0x2a ),
    isint( 42.0 ),
    isint( '42' ),
    isint( true ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false,
    false,
    false
]
```
