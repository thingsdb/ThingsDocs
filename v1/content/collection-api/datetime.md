---
title: "datetime"
weight: 205
---

Returns a [datetime](../../data-types/datetime) depending on some optional values.

This function does *not* generate a [change](../../overview/changes).

### Function

Interface | Arguments | Description
--------- | --------- | -----------
`datetime()`  | None | Return a `datetime` with the current date/tine.
`datetime(ts)` | `int`/`float` | Return a `datetime` from a given UNIX time stamp.
`datetime(str, [fmt])` | `str` | Return a `datetime` from a given string. See [initialize from string](./#initialize-from-string) for a details.
`datetime(int, int, int, [int, [int, [int]]], [zone])` | `int`, `int`,... `str` | Return a `datetime` using values for individual time units, with optional time zone.

### Initialize from string

The following formats will be understood by both the [datetime(..)](../datetime) and [timeval(..)](../timeval) functions
without an explicit format:

Format | Example | Description
-------|---------|------------
`YYYY` | `"2020"` | A `datetime` on the first of January at `00:00` in the given year using the [time zone](../../thingsdb-api/set_time_zone) from the collection.
`YYYY-mm` | `"2020-09"` | A `datetime` at the first of a given month and year, at `00:00` using the [time zone](../../thingsdb-api/set_time_zone) from the collection.
`YYYY-mm-dd` | `"2020-09-14"` | A `datetime` at the given date, at `00:00` using the [time zone](../../thingsdb-api/set_time_zone) from the collection.
`YYYY-mm-ddTHH` | `"2020-09-14T20"` | A `datetime` at the given date, at `HH:00` using the [time zone](../../thingsdb-api/set_time_zone) from the collection.
`YYYY-mm-ddTHH:MM` | `"2020-09-14T20:52"` | A `datetime` at the given date, at `HH:MM` using the [time zone](../../thingsdb-api/set_time_zone) from the collection.
`YYYY-mm-ddTHH:MM:SS` | `"2020-09-14T20:52:28"` | A `datetime` using the [time zone](../../thingsdb-api/set_time_zone) from the collection..
`YYYY-mm-ddTHH:MM:SSZ` | `"2020-09-14T20:52:28Z"` | A `datetime` using the Coordinated Universal Time (UTC).
`YYYY-mm-ddTHH:MM:SS+-hh` | `"2020-09-14T20:52:28+01"` | A `datetime` relative to the Coordinated Universal Time (UTC) with a given offset `+hh` or `-hh`.
`YYYY-mm-ddTHH:MM:SS+-hhmm` | `"2020-09-14T20:52:28+0100"` | A `datetime` with an offset relative to the Coordinated Universal Time (UTC).

{{% notice tip %}}
The `T` in the formats above is optional and may be replace with a space (` `).
{{% /notice %}}

Optionally, a second `fmt` argument may be given in which you may specify a custom format.
The most important field descriptors for the formatter are listed below. In case a string
(such as the name of a day of the week or a month name) is to be matched, the comparison is
case insensitive.  In case a number is to be matched, leading zeros are permitted but not required.

Specifier | Description
----------|------------
`%a` / `%A` | The name of the day, in abbreviated form or the full name.
`%b` / `%B`/ `%h` | The month name, in abbreviated form or the full name.
`%c` | The date and time representation, for example: `Thu Dec 10 13:50:28 2020`
`%C` | The century number (0–99).
`%d` / `%e` | The day of month (`1–31`).
`%D` | Equivalent to `%m/%d/%y` (American style date).
`%H` | The hour (`0–23`).
`%I` | The hour on a 12-hour clock (`1–12`).
`%j` | The day number in the year (`1–366`).
`%m` | The month number (`1–12`).
`%M` | The minute (`0–59`).
`%n` | Arbitrary whitespace.
`%p` | AM or PM.
`%r` | The 12-hour clock time, for example: `12:00:00 AM`
`%R` | Equivalent to `%H:%M`.
`%S` | The second (`0–59`).
`%t` | Arbitrary whitespace.
`%T` | Equivalent to `%H:%M:%S`.
`%U` | The week number with Sunday the first day of the week (`0–53`). The first Sunday of January is the first day of week 1.
`%w` | The ordinal number of the day of the week (`0–6`), with Sunday as `0`.
`%W` | The week number with Monday the first day of the week (`0–53`). The first Monday of January is the first day of week 1.
`%y` | The year within century (0–99).  When a century is not otherwise specified, values in the range `69–99` refer to years in the twentieth century, values in the range `00–68` refer to years in the twenty-first century.
`%Y` | The year, including century (for example, `2013`).


Example, creating a `datetime` object using a custom formatter:

```thingsdb,json_response
datetime('2013 37', '%Y %j');  // day 37 in the year 2013
```

> Return value in JSON format

```json
"2013-02-06T00:00:00Z"
```

### Return value

Returns a [datetime](../../data-types/datetime) object.

### Example

> This code shows a few examples for ***datetime()***:

```thingsdb,should_pass
[
    {datetime();                                    /* current time                 */ },
    {datetime(1607609782);                          /* Thu, 10 Dec 2020 14:16:22    */ },
    {datetime(2013, 2, 6, 12);                      /* Wed, 06 Feb 2013             */ },
    {datetime(2013, 2, 6, 13, 'Europe/Amsterdam');  /* with a time zone             */ },
    {datetime('1978-08-07T13:30:00Z');              /* Mon, 07 Aug 1978 13:30       */ },
    {datetime('12/10/2020', '%M/%s/%Y');            /* Thu, 10 Dec 2020             */ },
];
```

> Return value in JSON format with the collection time zone configured as UTC:

```json
[
    "2020-12-17T15:58:25Z",
    "2020-12-10T14:16:22Z",
    "2013-02-06T12:00:00Z",
    "2013-02-06T13:00:00+0100",
    "1978-08-07T13:30:00Z",
    "2020-01-01T00:00:10Z"
]
```