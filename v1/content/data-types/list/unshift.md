---
title: "unshift"
weight: 96
---

Adds new items to the start of a list, and returns the new length.

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`unshift(item1, item2, ..., itemX)`

### Return value

Returns the new length of the list.

### Example

> This code inserts values to the start of a list:

```thingsdb,json_response
list = [4, 5, 6];
list.unshift(1, 2, 3);  // Returns the new length, 6

list;
```

> Return value in JSON format

```json
[1, 2, 3, 4, 5, 6]
```
