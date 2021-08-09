---
title: "pop"
weight: 75
---

Removes the last item from a [list](../../list) and returns that item.

This function changes the length of the list. The `pop()` function works
on a `list` type array, but not on a `tuple` since tuples are immutable.

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`pop()`

### Arguments

None

### Return value

The removed item from the list. A [lookup_err()](../../../errors/lookup_err) is raised if the list is empty.

### Example

> This code show an example usage of ***pop()***:

```thingsdb,json_response
(list = [1, 2, 3]).pop();  // 3
list;
```

> Return value in JSON format

```json
[
    1,
    2
]
```
