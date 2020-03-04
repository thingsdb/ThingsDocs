---
title: "isinf"
weight: 118
---

This function determines whether the provided value is a positive or negative *infinity*.

This function does *not* generate an [event](../../overview/events).

### Function

`isinf(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a positive or negative *infinity*, else it returns `false`.

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
