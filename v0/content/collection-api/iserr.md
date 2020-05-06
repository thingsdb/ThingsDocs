---
title: "iserr"
weight: 122
---

This function determines whether the provided value is a [error](../../data-types/error) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`iserr(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is an error, else it returns `false`.

### Example

> This code shows some return values for ***iserr()***:

```thingsdb,json_response
[
    iserr( err() ),
    iserr( zero_div_err() ),
    iserr( try((1 / 0)) ),
    iserr( try((1 / 1)) ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    true,
    false
]
```
