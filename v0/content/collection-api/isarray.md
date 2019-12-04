---
title: "isarray"
weight: 98
---

This function determines whether the value passed to this function
is a [list](../../data-types/list) or [tuple](../../data-types/tuple) type or not. The functions [islist](../../collection-api/islist) and
[istuple](../../collection-api/istuple) can be used to check if the array is mutable.

This function does *not* generate an [event](../../overview/events).

### Function

`isarray(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested for being an array.

### Return value

Returns `true` the value passed is array else it returns `false`.

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
