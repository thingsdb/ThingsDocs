---
title: "yday"
weight: 50
---

Return the day in the year as an integer value between `0..365` where the first of January is day `0`.

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`yday()`

### Arguments

None

### Return value

Returns the day in the year as a number between `0` and `365`.

### Example

> This code uses `yday()` as an example:

```thingsdb,json_response
datetime(2020, 12, 10).yday();
```

> Return value in JSON format

```json
344
```
