---
title: "timeval"
weight: 167
---

Type `timeval` is exactly the same as type [datetime](../datetime). The only difference is the
default return. The return value of a `timeval` type is the value as a UNIX time stamp, while
type `datetime` returns with the time as a string in ISO8601 format.

Why type `timeval`? It is possible to return a `datetime` as `int(datetime)` to get the UNIX time stamp, so why use `timeval`?
It is often easier to work with time stamps then with time as string values.

Some

```thingsdb,json_response
tv = timeval(2020, 12, 10);   /* type timeval, 10 December 2020 */
dt = datetime(2020, 12, 10);  /* type datetime, 10 December 2020 */
assert (tv == dt);            /* true, both have the same time */
assert (type(tv) == 'timeval');
assert (type(dt) == 'datetime');
{
    dt: dt,
    tv: tv
};  // Return value is different
```

> Return value in JSON format

```json
{
    "dt": "2020-12-10T00:00:00Z",
    "tv": 1607558400
}
```

### Functions

Function | Description
------ | -----------
[extract](../datetime/extract) | Return a `thing` with `second`, `minute`, `hour`, `day`, `month`, `year` and `gmt_offset` as individual properties.
[format](../datetime/format) | Returns a string representation using a custom format string.
[move](../datetime/move) | Return a new `timeval` which is shifted in time relative to the original date/time.
[replace](../datetime/replace) | Return a new `timeval` with new values for given time units.
[to](../datetime/to) | Return a new `timeval` with new time zone information.
[week](../datetime/week) | Return the week of the year as an integer between `0..53`. Week `1` starts at the first Sunday in January.
[weekday](../datetime/weekday) | Return the number of days (`0..6`) since the last Sunday.
[yday](../datetime/yday) | Return the day in the year as an integer value between `0..365` where the first of January is day `0`.
[zone](../datetime/zone) | Return the time zone as a string, of `nil` if not zone information is available.

{{% notice info %}}
The above functions correspond to those of a `datetime` object. For that reason, they are only listed under the data type `datetime`.
{{% /notice %}}

### Related functions

Function | Description
------ | -----------
[timeval](../../collection-api/timeval) | Create a new timeval value.
[is_timeval](../../collection-api/is_timeval) | Test if a given value is of type timeval.
