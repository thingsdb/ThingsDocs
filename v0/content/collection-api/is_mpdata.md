---
title: "is_mpdata"
weight: 181
---

This function determines whether the provided value is an [integer](../../data-types/int) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`is_mpdata(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type [mpdata](../../data-types/), else it returns `false`.

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
