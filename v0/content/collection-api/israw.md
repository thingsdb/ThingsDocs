---
title: "israw"
weight: 116
---

This function determines whether the value passed to this function is of
type `str` *or* `bytes`.

This function does *not* generate an [event](../../overview/events).

### Function

`israw(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` is the given value is of type `str` *or* `bytes`, else `false`.

### Example

> This code shows some return values for ***israw()***:

```thingsdb,json_response
[
    israw( 'some string' ),
    israw( bytes('xxxx') ),
];
```

> Return value in JSON format

```json
[
    true,
    true
]
```
