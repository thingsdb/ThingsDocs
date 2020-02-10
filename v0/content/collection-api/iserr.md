---
title: "iserr"
weight: 109
---

This function determines whether the value passed to this function
is a [error](../../data-types/error) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`iserr(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is an error else it returns `false`.

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
