---
title: "is_int"
weight: 174
---

This function determines whether the provided value is an [integer](../../data-types/int) or not.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isint` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_int(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is an integer, else it returns `false`.

### Example

> This code shows some return values for ***is_int()***:

```thingsdb,json_response
[
    is_int( 42 ),
    is_int( 0x2a ),
    is_int( 42.0 ),
    is_int( '42' ),
    is_int( true ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false,
    false,
    false
]
```
