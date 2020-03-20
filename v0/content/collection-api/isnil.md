---
title: "isnil"
weight: 127
---

This function determines whether the provided value is [nil](../../data-types/nil).

This function does *not* generate an [event](../../overview/events).

### Function

`isnil(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is `nil`, else `false`.

### Example

> This code shows some return values for ***isnil()***:

```thingsdb,json_response
[
    isnil( nil ),
    isnil( 0 ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
