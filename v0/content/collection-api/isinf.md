---
title: "isinf"
weight: 108
---

This function determines whether the value passed to this function
is a positive or negative *infinity*.

This function does *not* generate an [event](../../overview/events).

### Function

`isinf(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is a positive or negative *infinity* else it returns `false`.

### Example

> This code shows some return values for ***isinf()***:

```thingsdb,json_response
[
    isinf( -inf ),
    isinf( inf ),
    isinf( 0 ),
    isinf( nan ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false,
    false
]
```
