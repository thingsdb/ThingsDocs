---
title: "push"
weight: 90
---

Adds new items to the end of a list, and returns the new length.

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`push(item1, item2, ..., itemX)`

### Return value

Returns the new length of the list.

### Example

> This code pushes values to a list:

```thingsdb,json_response
list = [1, 2, 3];
list.push(4, 5, 6);  // Returns the new length, 6

list;
```

> Return value in JSON format

```json
[1, 2, 3, 4, 5, 6]
```
