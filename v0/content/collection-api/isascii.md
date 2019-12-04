---
title: "isascii"
weight: 98
---

This function determines whether the value passed to this function is of
type [str](../../data-types/str) and contains only valid ascii characters.

This function does *not* generate an [event](../../overview/events).

### Function

`isascii(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the given value is of type `str` and contains only ascii characters, else `false`.

### Example

> This code shows some return values for ***isascii()***:

```thingsdb,json_response
[
    isascii( 'ԉ' ),
    isascii( 'pi' ),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
