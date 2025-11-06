---
title: "is_mpdata"
weight: 248
---

This function determines whether the provided value is of type [mpdata](../../../data-types/) or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_mpdata(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type [mpdata](../../../data-types/), else it returns `false`.

### Example

> This code shows some return values for ***is_mpdata()***:

```thingsdb,json_response,@t
[
    is_mpdata( user_info("admin") ),
    is_mpdata( user_info("admin").load() ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
