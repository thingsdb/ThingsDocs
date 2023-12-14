---
title: "week"
weight: 47
---

Return the week of the year as an integer between `0..53`. Week `1` starts at the first Sunday in January.

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`week()`

### Arguments

None

### Return value

Returns the week in the year as a number between `0` and `53`.

### Example

> This code uses `week()` as an example:

```thingsdb,json_response
datetime(2020, 12, 10).week();
```

> Return value in JSON format

```json
49
```
