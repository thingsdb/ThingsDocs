---
title: "extract"
weight: 40
---

Return a `thing` with `second`, `minute`, `hour`, `day`, `month`, `year` and `gmt_offset` as individual properties.

It is possible to get a single property by using the name of the property as the first argument.

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`extract([key])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`key` | `str` (optional) | May be a specific property, one of `second`, `minute`, `hour`, `day`, `month`, `year` or `gmt_offset`.


### Return value

Returns a thing or the value for a specific property.

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

> Another example to get the `gmt_offset` only with `extract()`:

```thingsdb,json_response
datetime(2013, 2, 6, 13, 12, 28, 'Europe/Amsterdam').extract('gmt_offset');
```

> Return value in JSON format

```json
3600
```
