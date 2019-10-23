---
title: "keys"
date: 2019-10-23T14:57:32+02:00
weight: 6
---

## keys

Returns an array with all the property names of a [thing](../../thing).
The same could be returned using map so the following statement is `true`:

`.keys() == .map(|k| k)`

{{% notice warning %}}
Although the `keys()` and `map()` functions in the example above will return an array with the same order,
the order of *keys* in the array is not guaranteed and may be different each time you run the query.
{{% /notice %}}

This function does *not* generate an [event](../../../events).

### Function
*thing*.`keys()`

### Arguments
None

### Return value
Returns an array with property names.

> This code shows how to use `keys()`:

```thingsdb,json_response
{a: 1, b: 2, c: 3}.keys();
```

> Return value in JSON format (Warning: the order is *NOT* guaranteed)

```json
[
    "a",
    "b",
    "c"
]
```
