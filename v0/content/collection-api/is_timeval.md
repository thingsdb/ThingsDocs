---
title: "is_timeval"
weight: 190
---

This function determines whether the provided value is of
type [timeval](../../data-types/timeval).

This function does *not* generate an [event](../../overview/events).


### Function

`is_timeval(value)`

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
    is_timeval( timeval(2013, 2, 6) ),
    is_timeval( datetime(2013, 2, 6) ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
