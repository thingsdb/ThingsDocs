---
title: "isfloat"
weight: 110
---

This function determines whether the value passed to this function
is a [floating point](../../data-types/float) value or not.

This function does *not* generate an [event](../../overview/events).

### Function

`isfloat(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is a float else it returns `false`.

### Example

> This code shows some return values for ***isfloat()***:

```thingsdb,json_response
[
    isfloat( 42.0 ),
    isfloat( 0.42e+2 ),
    isfloat( 42 ),
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
