---
title: "is_raw"
weight: 189
---

This function determines whether the provided value is of
type `str` *or* `bytes`.

This function does *not* generate an [event](../../overview/events).

### Function

`is_raw(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str` *or* `bytes`, else `false`.

### Example

> This code shows some return values for ***is_raw()***:

```thingsdb,json_response
[
    is_raw( 'some string' ),
    is_raw( bytes('xxxx') ),
];
```

> Return value in JSON format

```json
[
    true,
    true
]
```
