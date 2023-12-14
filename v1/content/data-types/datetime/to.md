---
title: "to"
weight: 48
---

Return a new [datetime](../) (or [timeval](../../timeval)) object with new time zone information.
Note that the proper time does not change, only the time zone will change.

See [time_zones_info()](../../../thingsdb-api/time_zones_info/#available-time-zones) for a list of all available time zones.

{{% notice warning %}}
If zone information is given using a fixed offset (`+hh[mm]` or `-hh[mm]`), then the new `datetime` object has no proper time zone information and thus has no
*day-light-saving* information.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`to(zone)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`zone` | `str` (required) | May be a time zone like `Europe/Amsterdam`, `UTC `or the format `+hh[mm]` / `-hh[mm]`.

### Return value

Returns a new `datetime` (or `timeval`) object.

### Example

> This code uses `to()` as an example:

```thingsdb,json_response
datetime('2020-12-10T16:08:24Z').to('Europe/Kyiv');
```

> Return value in JSON format

```json
"2020-12-10T18:08:24+0200"
```
