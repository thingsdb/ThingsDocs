---
title: "isnan"
weight: 106
---

This function determines whether the value passed to this function is a number.

This function does *not* generate an [event](../../overview/events).

### Function

`isnan(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the given value is not a number, else `false`.

### Example

> This code shows some return values for ***isnan()***:

```thingsdb,json_response
[
    isnan( true ),
    isnan( 123 ),
    isnan( 3.14 ),
    isnan( inf ),
    isnan( [] ),
    isnan( {} ),
    isnan( nan ),
    isnan( '123' ),
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
