---
title: "timeval"
weight: 294
---

Returns a [timeval](../../data-types/timeval) depending on some optional values.

This function does *not* generate a [change](../../overview/changes).

### Function

Interface | Arguments | Description
--------- | --------- | -----------
`timeval()`  | None | Return a `timeval` with the current date/tine.
`timeval(ts)` | `int`/`float` | Return a `timeval` from a given UNIX time stamp.
`timeval(str, [fmt])` | `str` | Return a `timeval` from a given string. See [initialize from string](../datetime/#initialize-from-string) for a details.
`datetime(int, int, int, [int, [int, [int]]], [zone])` | `int`, `int`,... `str` | Return a `timeval` using values for individual time units, with optional time zone.

### Return value

Returns a [timeval](../../data-types/timeval) object.

### Example

> This code shows a few examples for ***timeval()***:

```thingsdb,should_pass
[
    {timeval();                                     /* current time                 */ },
    {timeval(1607609782);                           /* Thu, 10 Dec 2020 14:16:22    */ },
    {timeval(2013, 2, 6, 12);                       /* Wed, 06 Feb 2013             */ },
    {timeval(2013, 2, 6, 13, 'Europe/Amsterdam');   /* with a time zone             */ },
    {timeval('1978-08-07T13:30:00Z');               /* Mon, 07 Aug 1978 13:30       */ },
    {timeval('12/10/2020', '%M/%s/%Y');             /* Thu, 10 Dec 2020             */ },
];
```

> Return value in JSON format with the collection time zone configured as UTC:

```json
[
    1607610966,
    1607609782,
    1360152000,
    1360152000,
    271344600,
    1577836810
]
```
