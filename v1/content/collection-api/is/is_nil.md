---
title: "is_nil"
weight: 247
---

This function determines whether the provided value is [nil](../../../data-types/nil).

This function does *not* generate a [change](../../../overview/changes).

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
