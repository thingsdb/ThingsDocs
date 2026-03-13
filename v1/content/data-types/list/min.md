---
title: "min"
weight: 107
---

Returns the minimum value from a list.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`min()`

### Arguments

None

### Return value

The minimum value of all values in a list. A [lookup_err()](../../../errors/lookup_err) is raised if the list is empty.

### Example

> This code shows an example using ***min()***:

```thingsdb,json_response
["lemon", "apple", "cherry", "orange"].min();
```

> Return value in JSON format

```json
"apple"
```
