---
title: "is_str"
weight: 231
---

This function determines whether the provided value is of
type [str](../../data-types/str).

The value is *not* explicitly checked for valid UTF-8 characters, use [is_utf8()](../is_utf8) if you want to check for valid UTF-8 data.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_str(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str`, else `false`.

### Example

> This code shows some return values for ***is_utf8()***:

```thingsdb,json_response
[
    is_str( 'ԉ' ),
    is_str( 'pi' ),
];
```

> Return value in JSON format

```json
[
    true,
    true
]
```
