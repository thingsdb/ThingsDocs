---
title: "weekday"
weight: 51
---

Return the number of days (`0..6`) since the last Sunday.

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`weekday()`

### Arguments

None

### Return value

Returns the day of the week as a number between `0` (Sunday) and `6`.

### Example

> This code uses `weekday()` as an example:

```thingsdb,json_response
datetime(2020, 12, 10).weekday();
```

> Return value in JSON format

```json
4
```


