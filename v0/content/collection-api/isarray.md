---
title: "isarray"
weight: 117
---

This function determines whether the provided value is of type [list](../../data-types/list) or [tuple](../../data-types/tuple) or not. The functions [islist](../../collection-api/islist) and
[istuple](../../collection-api/istuple) can be used to check if the array is mutable.

This function does *not* generate an [event](../../overview/events).

### Function

`isarray(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the value passed is an array, else it returns `false`.

### Example

> This code shows some return values for ***isarray()***:

```thingsdb,json_response
[
    isarray( [] ),
    isarray( tmp = [['nested']] ),
    isarray( tmp[0] ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    true
]
```
