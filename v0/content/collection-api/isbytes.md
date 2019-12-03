---
title: "isbytes"
weight: 98
---

This function determines whether the value passed to this function
is of type [bytes](../../data-types/bytes) or not.

This function does *not* generate an [event](../../overview/events).

### Function

`isbytes(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the passed value is of type `bytes` else it returns `false`.

### Example

> This code shows some return values for ***isbytes()***:

```thingsdb,json_response
[
    isbytes( bytes() ),
    isbytes( 'abc' ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
