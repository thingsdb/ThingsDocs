---
title: "isthing"
weight: 136
---

This function determines whether the value passed to this function
is a [thing](../../data-types/thing) or not.

This function does *not* generate an [event](../../events).

### Function

`isthing(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is a thing else it returns `false`.

> This code shows some return values for ***isthing()***:

```thingsdb,json_response
[
    isthing( {} ),
    isthing( [] ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
