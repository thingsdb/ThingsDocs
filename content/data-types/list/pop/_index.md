---
title: "pop"
date: 2019-10-23T12:52:11+02:00
weight: 8
---

Removes the last element from a [list](../../list) and returns that element.
This method changes the length of the list. The `pop()` method works
on a `list` type array, but not on a `tuple` since tuples are immutable.

This function generates an [event](../../../events).

### Function

*list*.`pop()`

### Arguments

None

### Return value

The removed element from the list. An `INDEX_ERROR` is raised if the list is empty.

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
