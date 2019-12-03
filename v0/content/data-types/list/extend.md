---
title: "extend"
weight: 31
---

Adds a [list](..) or [tuple](../../tuple) with items to the end of a [list](..), and returns the new length.

This function generates an [event](../../../overview/events).

### Function

*list*.`extend(list)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
list | list/tuple | The `list` or `tuple` to extend the `list` with.

### Return value

Returns the new length of the list.

### Example

> This code extends a list with a given array:

```thingsdb,json_response
a = [1, 2, 3];
b = [4, 5, 6];
a.extend(b);  // returns the new length, 6
a;
```

> Return value in JSON format

```json
[
    1,
    2,
    3,
    4,
    5,
    6
]
```
