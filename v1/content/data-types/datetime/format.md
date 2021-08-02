---
title: "format"
weight: 38
---

Returns a string representation for a `datetime` object using a custom format.

This function does *not* generate a [change](../../../overview/changes).

### Function

*datetime*.`format(fmt)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
`fmt` | str (required) | Custom output format.

### Format specifiers

The following specifiers may be used:

Specifier | Example | Description
--------- | ------- | -----------
`%a` | `Wed` | Abbreviated weekday name. **\***
`%A` | `Wednesday` | Full weekday name. **\***
`%b` | `Feb` | Abbreviated month name. **\***
`%B` | `February` | Full month name. **\***
`%c` | `Wed Feb  6 00:00:00 2013` | Date and time representation. **\***
`%C` | `20` | Year divided by 100 as integer (`00-99`).
`%d` | `06` | Day of the month, zero-padded (`01-31`).
`%D` | `02/06/13` | Equivalent to `%m/%d/%y`.
`%e` | `6` | Day of the month, space-padded (`1-31`).
`%F` | `2013-02-06` | Equivalent to `%Y-%m-%d`.
`%g` | `13` | Week-based year, last two digits (`00-99`)
`%G` | `2013` | Week-based year.
`%h` | `Feb` | Abbreviated month name (same as `%b`). **\***
`%H` | `14` | Hour in 24h format (`00-23`).
`%I` | `02` | Hour in 12h format (`01-12`).
`%j` | `037` | Day of the year (`001-366`).
`%m` | `02` | Month as a decimal number (`01-12`).
`%M` | `12` | Minute (`00-59`).
`%n` | `\n` | New-line character (`\n`).
`%p` | `PM` | AM or PM.
`%r` | `02:12:28 PM` | 12-hour clock time. **\***
`%R` | `14:12` | 24-hour HH:MM time, equivalent to `%H:%M`.
`%S` | `28` | Second (`00-61`).
`%t` | `\t` | Horizontal-tab character (`\t`).
`%T` | `14:12:28` | ISO 8601 time format (HH:MM:SS), equivalent to `%H:%M:%S`.
`%u` | `3` | ISO 8601 weekday as number with Monday as 1 (`1-7`).
`%U` | `05` | Week number with the first Sunday as the first day of week one (`00-53`).
`%V` | `06` | ISO 8601 week number (`01-53`).
`%w` | `3` | Weekday as a decimal number with Sunday as `0` (`0-6`).
`%W` | `05` | Week number with the first Monday as the first day of week one (`00-53`).
`%x` | `02/06/13` | Date representation. **\***
`%X` | `14:12:28` | Time representation. **\***
`%y` | `13` | Year, last two digits (`00-99`).
`%Y` | `2013` | Year.
`%z` | `+0000` | ISO 8601 offset from UTC in timezone (1 minute=1, 1 hour=100).
`%Z` | `UTC` | Timezone name or abbreviation. This may differ from `zone()` since the latter returns the ThingsDB zone information instead of local time zone info. **\***
`%%` | `%` | A `%` sign

{{% notice info %}}
Specifiers marked with an asterisk (**\***) depend on local settings of the ThingsDB node.
{{% /notice %}}

### Return value

Returns the datetime as a formatted string.

### Example

> This code uses `format()` as an example:

```thingsdb,json_response
datetime(2013, 2, 6, 13, 12, 'Europe/Amsterdam').format('%A, %d %B %Y at %R (%z)');
```

> Return value in JSON format

```json
"Wednesday, 06 February 2013 at 13:12 (+0100)"
```
