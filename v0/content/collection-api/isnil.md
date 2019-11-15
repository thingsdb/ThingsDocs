---
title: "isnil"
date: 2019-10-14T13:53:26+02:00
weight: 1900
---

This function determines whether the value passed to this function is [nil](../../data-types/nil).

This function does *not* generate an [event](../../events).

### Function

`isnil(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the given value is `nil`, else `false`.

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
