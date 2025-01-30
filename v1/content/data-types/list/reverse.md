---
title: "reverse"
weight: 100
---

The function returns a new list with items in reverse order.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`reverse()`

### Arguments

None

### Return value

A new list in reverse order.

### Examples

> Simple sort

```thingsdb,json_response
// return a range in reverse order
range(5).reverse()
```

> Return value in JSON format

```json
[
    4,
    3,
    2,
    1,
    0
]
```
