---
title: "is_future"
weight: 205
---

This function determines whether the provided value is a [future](../../data-types/future) value or not.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_future(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a future, else it returns `false`.

### Example

> This code shows some return values for ***is_float()***:

```thingsdb,json_response
[
    is_future( future(nil) ),
    is_future( future(nil).then(||nil) ),
    is_future( ||nil ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false
]
```
