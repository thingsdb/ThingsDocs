---
title: "istuple"
weight: 148
---

This function determines whether the provided value is a [tuple](../../data-types/tuple) or not. At least nested arrays are of kind tuple.

This function does *not* generate an [event](../../overview/events).

### Function

`istuple(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a tuple, else it returns `false`.

### Example

> This code shows some return values for ***istuple()***:

```thingsdb,json_response
[
    istuple( [] ),
    istuple( tmp = [['nested'], set()] ),
    istuple( tmp[0] ),
    istuple( tmp[1] ),
];
```

> Return value in JSON format

```json
[
    false,
    false,
    true,
    true
]
```
