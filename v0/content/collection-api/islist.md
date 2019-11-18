---
title: "islist"
weight: 128
---

This function determines whether the value passed to this function
is a [list](../../data-types/list) or not.

This function does *not* generate an [event](../../events).

### Function

`islist(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is a `list`, else it returns `false`.

### Example

> This code shows some return values for ***islist()***:

```thingsdb,json_response
[
    islist( [] ),
    islist( tmp = [['nested']] ),
    islist( tmp[0] ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false
]
```
