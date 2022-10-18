---
title: "is_time_zone"
weight: 237
---

This function determines whether the provided value is of
type [str](../../data-types/str) and contains a valid time zone *(see [time_zones_info()](../time_zones_info) for a list with all available time zones)*.

This function does *not* generate a [change](../../overview/changes).

### Function

`is_time_zone(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type `str` and contains a valid time zone, else `false`.

### Example

> This code shows some return values for ***is_time_zone()***:

```thingsdb,json_response
[
    is_time_zone( 'Europe/Amsterdam' ),
    is_time_zone( '@Work' ),
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
