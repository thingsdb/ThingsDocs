---
title: "has"
weight: 80
---

Determines if a [list](..) or [tuple](../../tuple) has a given value.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`has(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | Value to check.

### Return value

Returns `true` if the given value is found in the list and otherwise `false`.

### Example

> This code shows an example use case of ***has()***:

```thingsdb,json_response
months = ["January", "February", "March", "April"];
[
    months.has("March"),
    months.has("May")
];
```

> Return value in JSON format

```json
[
    true,
    false
]
```
