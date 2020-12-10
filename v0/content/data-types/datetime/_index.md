---
title: "datetime"
weight: 36
---

Type `datetime` can be used to store a value with date and time information.

{{% notice note %}}
The `datetime` and `timeval` types have *second* precision. If more than *second* precision is required you will have to
use your own type. For example the function [now()](../../collection-api/now) returns the current time-stamp as a floating point type.
{{% /notice %}}


### Functions

Function | Description
------ | -----------
[extract](../datetime/extract) | Return a `thing` with `second`, `minute`, `hour`, `day`, `month`, `year` and `gmt_offset` as individual properties.
[format](../datetime/format) | Returns a string representation using a custom format string.
[move](../datetime/move) | Return a new `datetime` which is shifted in time relative to the original date/time.
[replace](../datetime/replace) | Return a new `datetime` with new values for given time units.
[to](../datetime/to) | Return a new `datetime` with new time zone information.
[week](../datetime/week) | Return the week of the year as an integer between `0..53`. Week `1` starts at the first Sunday in January.
[weekday](../datetime/weekday) | Return the number of days (`0..6`) since the last Sunday.
[yday](../datetime/yday) | Return the day in the year as an integer value between `0..365` where the first of January is day `0`.
[zone](../datetime/zone) | Return the time zone as a string, of `nil` if not zone information is available.

