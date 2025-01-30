---
title: "is_datetime"
weight: 236
---

This function determines whether the provided value is of
type [datetime](../../../data-types/datetime).

This function does *not* generate a [change](../../../overview/changes).


### Function

`is_datetime(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `timeval`, else `false`.

### Example

> This code shows some return values for ***is_utf8()***:

```thingsdb,json_response
[
    is_datetime( timeval(2013, 2, 6) ),
    is_datetime( datetime(2013, 2, 6) ),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
