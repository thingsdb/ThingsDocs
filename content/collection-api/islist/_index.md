---
title: "islist"
date: 2019-10-14T10:01:56+02:00
weight: 29
---

This function determines whether the value passed to this function
is a mutable [array](../../data-types/array-type) or not.

This function does *not* generate an [event](../../events).

### Function
`islist(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the passed value is a `list`, else it returns `false`.

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
