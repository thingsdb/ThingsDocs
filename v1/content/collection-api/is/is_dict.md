---
title: "is_dict"
weight: 245
---

This function determines whether the provided value is a [dict](../../../data-types/dict) value or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_dict(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type dict, else it returns `false`.

### Example

> This code shows some return values for ***is_dict()***:

```thingsdb,json_response
[
    is_dict( dict() ),
    is_dict( {} ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
