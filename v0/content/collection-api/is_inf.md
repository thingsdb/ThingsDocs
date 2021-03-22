---
title: "is_inf"
weight: 177
---

This function determines whether the provided value is a positive or negative *infinity*.

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isinf` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_inf(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a positive or negative *infinity*, else it returns `false`.

### Example

> This code shows some return values for ***is_inf()***:

```thingsdb,json_response
[
    is_inf( -inf ),
    is_inf( inf ),
    is_inf( 0 ),
    is_inf( nan ),
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
