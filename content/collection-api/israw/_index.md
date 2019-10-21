---
title: "israw"
date: 2019-10-14T10:02:14+02:00
weight: 32
---

This function determines whether the value passed to this function is of
type `raw`.

This function does *not* generate an [event](../../events).

### Function
`israw(value)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value
Returns `true` is the given value is of type `raw`, else `false`.

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
