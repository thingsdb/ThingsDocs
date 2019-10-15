---
title: "values"
date: 2019-10-14T10:06:20+02:00
weight: 60
---

Returns an array with all the property values of a [thing](../../thingsdb-api).
The same could be returned using map so the following statement is `true`:

`(.values() == .map(|_, v| v))`

{{% notice warning %}}
Although the `values()` and `map()` in the example above will return an array with the same order,
the order of *values* in the array is not guaranteed and may be different each time you run the query.
{{% /notice %}}

This function does *not* generate an [event](../../events).

### Function
*thing*.`values()`

### Arguments
None

### Return value
Returns an array with property values.

> This code shows how to use `values()`:

```
{a: 1, b: 2, c: 3}.values();
```

> Return value in JSON format (Warning: the order is *NOT* guaranteed)

```json
[
    1,
    2,
    3
]
```
