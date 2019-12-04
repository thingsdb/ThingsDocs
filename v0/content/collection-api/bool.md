---
title: "bool"
weight: 91
---

Returns an [bool](../../data-types/bool) from a specified value.
If no value is given, `false` is returned.

Types with a *length* evaluate to `true` when the length is *not* `0` and `false` otherwise.

This function does *not* generate an [event](../../overview/events).

### Function

`bool(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (optional) | The value where to return a boolean value for.

### Return value

A boolean value.

### Example

> This code shows some return values for ***bool()***:

```thingsdb,json_response
[
    bool(),
    bool(nil),
    bool({}),
    bool({answer: 42}),
    bool([]),
    bool([1, 2, 3]),
    bool(''),
    bool('forty two'),
];
```

> Return value in JSON format

```json
[
    false,
    false,
    false,
    true,
    false,
    true,
    false,
    true
]
```
