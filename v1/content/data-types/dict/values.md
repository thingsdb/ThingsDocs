---
title: "values"
weight: 72
---

Returns a list containing all the values of the [dict](..).

{{% notice warning %}}
The order of *values* in the list is not guaranteed and may be different each time you run the query.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`values()`

### Arguments

None

### Return value

Returns a list with the values of a dict.

### Example

> This code shows how to use `values()`:

```thingsdb,json_response
dict([
    [uuid("00000000-0000-0000-0000-000000000000"), 'UUIDs can be used as keys'],
    [-1, 'Integer keys can be negative'],
    ["#", "Even hashes (#) as keys are allowed"],
]).values();
```

> Return value in JSON format (Warning: the order is *NOT* guaranteed)

```json
[
    "UUIDs can be used as keys",
    "Integer keys can be negative",
    "Even hashes (#) as keys are allowed"
]
```
