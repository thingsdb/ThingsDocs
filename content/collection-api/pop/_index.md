---
title: "pop"
date: 2019-10-14T10:03:42+02:00
weight: 43
---

Removes the last element from an [array](../../data-types/array-type) and returns that element.
This method changes the length of the array. The `pop()` method works
on a `list` type array, but not on a `tuple` since tuples are immutable.

This function generates an [event](../../events).

### Function
*list*.`pop()`

### Arguments
None

### Return value
The removed element from the array. An `INDEX_ERROR` is raised if the array is empty.

> This code show an example usage of ***pop()***:

```thingsdb,json_response
(arr = [1, 2, 3]).pop();
arr;
```

> Return value in JSON format

```json
[
    1,
    2
]
```
