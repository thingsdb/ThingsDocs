---
title: "zone"
weight: 55
---

Return zone information as a string about the [datetime](../) (or [timeval](../../timeval)) object.
If no zone information is available, `nil` will be returned.

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`zone()`

### Arguments

None

### Return value

Returns zone information or `nil` if no zone information is available.

### Example

> This code uses `zone()` as an example:

```thingsdb,json_response
[
    datetime().zone(),
    datetime().to('Europe/Amsterdam').zone(),
    datetime().to('+00').zone(),
]
```

> Return value in JSON format

```json
[
    "UTC",
    "Europe/Amsterdam",
    null
]
```
