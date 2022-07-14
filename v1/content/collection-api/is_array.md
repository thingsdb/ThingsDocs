---
title: "is_array"
weight: 206
---

This function determines whether the provided value is of type [list](../../data-types/list) or [tuple](../../data-types/tuple) or not. The functions [is_list](../../collection-api/is_list) and
[is_tuple](../../collection-api/is_tuple) can be used to check if the array is mutable.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_array(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the value passed is an array, else it returns `false`.

### Example

> This code shows some return values for ***is_array()***:

```thingsdb,json_response
[
    is_array( [] ),
    is_array( tmp = [['nested']] ),
    is_array( tmp[0] ),
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
