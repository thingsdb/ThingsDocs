---
title: "extract"
weight: 37
---

Return a `thing` with `second`, `minute`, `hour`, `day`, `month`, `year` and `gmt_offset` as individual properties.

This function does *not* generate an [event](../../../overview/events).

### Function

*datetime*.`extract()`

### Arguments

None

### Return value

Returns a thing.

### Example

> This code uses `extract()` as an example:

```thingsdb,json_response
datetime(2013, 2, 6, 13, 12, 28, 'Europe/Amsterdam').extract();
```

> Return value in JSON format

```json
{
    "day": 6,
    "gmt_offset": 3600,
    "hour": 13,
    "minute": 12,
    "month": 2,
    "second": 28,
    "year": 2013
}
```
