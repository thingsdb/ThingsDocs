---
title: "is_ascii"
weight: 218
---

This function determines whether the provided value is of
type [str](../../../data-types/str) and contains only valid ascii characters.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_ascii(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str` and contains only ascii characters, else `false`.

### Example

> This code shows some return values for ***is_ascii()***:

```thingsdb,json_response
[
    is_ascii( 'ԉ' ),
    is_ascii( 'pi' ),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
