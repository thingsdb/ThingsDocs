---
title: "is_bytes"
weight: 235
---

This function determines whether the provided value is of type [bytes](../../../data-types/bytes) or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_bytes(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `bytes`,  else it returns `false`.

### Example

> This code shows some return values for ***is_bytes()***:

```thingsdb,json_response
[
    is_bytes( bytes() ),
    is_bytes( 'abc' ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
