---
title: "replace"
weight: 40
---

Return a new [datetime](../) (or [timeval](../../timeval)) object with altered properties.
The new properties must be given by a [thing](../../thing).

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`replace(values)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`values` | `thing` (required) | Only the properties `year`, `month`, `day`, `hour`, `minute`, `second` will be used, all other properties are simply ignored.

### Return value

Returns a new `datetime` (or `timeval`) object.

### Example

> This code uses `replace()` as an example:

```thingsdb,json_response
datetime('2020-12-10T16:08:24Z').replace({
    minute: 0,
    second: 0,
});
```

> Return value in JSON format

```json
"2020-12-10T16:00:00Z"
```
