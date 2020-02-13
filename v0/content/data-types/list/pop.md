---
title: "pop"
weight: 44
---

Removes the last element from a [list](../../list) and returns that element.

This method changes the length of the list. The `pop()` method works
on a `list` type array, but not on a `tuple` since tuples are immutable.

This function generates an [event](../../../overview/events).

### Function

*list*.`pop()`

### Arguments

None

### Return value

The removed element from the list. A [lookup_err()](../../../errors/lookup_err) is raised if the list is empty.

### Example

> This code show an example usage of ***pop()***:

```thingsdb,json_response
(list = [1, 2, 3]).pop();
list;
```

> Return value in JSON format

```json
[
    1,
    2
]
```
