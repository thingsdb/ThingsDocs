---
title: "unique"
weight: 84
---

This function returns a *new* list where each item in the list is unique. If duplicated items are found, the first item will be retained.

An item in the list is marked as a duplicate when an item is compared as equal to another item using the `==` operator.

This function does *not* generate a [change](../../../overview/changes).

### Function

*list*.`unique()`


### Arguments

None

### Return value

Returns a *new* list where each item in the list is unique. The original list stays untouched.

### Example

> This code shows an example of ***unique()***:

```thingsdb,json_response
["tic", "tac", "tic", "toe"].unique();  // the second `tic` will not be retained in the new list
```

> Return value in JSON format

```json
[
    "tic",
    "tac",
    "toe"
]
```
