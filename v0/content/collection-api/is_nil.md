---
title: "is_nil"
weight: 168
---

This function determines whether the provided value is [nil](../../data-types/nil).

This function does *not* generate an [event](../../overview/events).

{{% notice warning %}}
This function has a deprecated alias `isnil` which will be removed in the next *minor* release.
{{% /notice %}}

### Function

`is_nil(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is `nil`, else `false`.

### Example

> This code shows some return values for ***is_nil()***:

```thingsdb,json_response
[
    is_nil( nil ),
    is_nil( 0 ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
