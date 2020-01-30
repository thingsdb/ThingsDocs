---
title: "isstr"
weight: 116
---

This function determines whether the value passed to this function is of
type [str](../../data-types/str).

The value is *not* explicitly checked for valid UTF-8 characters, use [isutf8()](../isutf8) if you want to check for valid UTF-8 data.

This function does *not* generate an [event](../../overview/events).

### Function

`isstr(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the given value is of type `str`, else `false`.

### Example

> This code shows some return values for ***isutf8()***:

```thingsdb,json_response
[
    isstr( 'ԉ' ),
    isstr( 'pi' ),
];
```

> Return value in JSON format

```json
[
    true,
    true
]
```
