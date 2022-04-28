---
title: "is_err"
weight: 211
---

This function determines whether the provided value is a [error](../../data-types/error) or not.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_err(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is an error, else it returns `false`.

### Example

> This code shows some return values for ***is_err()***:

```thingsdb,json_response
[
    is_err( err() ),
    is_err( zero_div_err() ),
    is_err( try((1 / 0)) ),
    is_err( try((1 / 1)) ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    true,
    false
]
```
