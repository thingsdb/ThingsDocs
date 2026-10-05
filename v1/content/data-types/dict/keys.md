---
title: "keys"
weight: 67
---

Returns a list containing all the keys of the [dict](..).

{{% notice warning %}}
The order of *keys* in the list is not guaranteed and may be different each time you run the query.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`keys()`

### Arguments

None

### Return value

Returns a list with the keys of a dict.

### Example

> This code shows how to use `keys()`:

```thingsdb,json_response
dict([
    [uuid("00000000-0000-0000-0000-000000000000"), 'UUIDs can be used as keys'],
    [-1, 'Integer keys can be negative'],
    ["#", "Even hashes (#) as keys are allowed"],
]).keys();
```

> Return value in JSON format (Warning: the order is *NOT* guaranteed)

```json
[
    "00000000-0000-0000-0000-000000000000",
    -1,
    "#"
]
```
