---
title: "is_closure"
weight: 214
---

This function determines whether the provided value is a [closure](../../data-types/closure) or not.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_closure(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a closure, else it returns `false`.

### Example

> This code shows some return values for ***is_closure()***:

```thingsdb,json_response
[
    is_closure( || nil ),
    is_closure( nil ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
