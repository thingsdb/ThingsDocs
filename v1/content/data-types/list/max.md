---
title: "max"
weight: 107
---

Returns the maximum value from a list.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`max()`

### Arguments

None

### Return value

The maximum value of all values in a list. A [lookup_err()](../../../errors/lookup_err) is raised if the list is empty.

### Example

> This code shows an example using ***max()***:

```thingsdb,json_response
[1, 4, 2, 9, 7, 8, 9, 3, 1].max();
```

> Return value in JSON format

```json
9
```
