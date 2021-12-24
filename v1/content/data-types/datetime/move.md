---
title: "move"
weight: 41
---

Return a new [datetime](../) (or [timeval](../../timeval)) object, which is shifted in time relative to the original date/time.
The amount the new date/time will be shifted must be given by one of the following units: `years`, `months`, `weeks`, `days`, `hours`, `minutes` or `seconds`.

{{% notice note %}}
When using `years` of `months` as a *unit*, it might not be possible to *move* to the exact same day in the month. If this is the case, the last possible day of the month will be used.
For example: `datetime(2020, 2, 29).move('years', -1);` return with `datetime(2019, 2, 28)` since the year 2019 does not have a 29th of February.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`move(unit, num)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`unit` | `str` (required) | One of `years`, `months`, `weeks`, `days`, `hours`, `minutes` or `seconds`.
`num` | `int` (required) | How many times to move the `unit`. A negative number will return a `datetime` or `timeval` in the past, relative to the original.

### Return value

Returns a new `datetime` (or `timeval`) object.

### Example

> This code uses `move()` as an example:

```thingsdb,json_response
datetime('2020-12-10').move('weeks', 2);
```

> Return value in JSON format

```json
"2020-12-24T00:00:00Z"
```
