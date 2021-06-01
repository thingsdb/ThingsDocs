---
title: "is_utf8"
weight: 195
---

This function determines whether the provided value is of
type [str](../../data-types/str) and contains valid UTF-8 characters.

This function does *not* generate an [event](../../overview/events).

### Function

`is_utf8(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `raw` and contains valid utf8, else `false`.

### Example

> This code shows some return values for ***is_utf8()***:

```thingsdb,json_response
[
    is_utf8( 'ԉ' ),
    is_utf8( 'pi' ),
];
```

> Return value in JSON format

```json
[
    true,
    true
]
```
