---
title: "clear"
weight: 67
---

Removes all items from a [list](..).

This function generates a [change](../../../overview/changes)

### Function

*list*.`clear()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> This code adds things to a set:

```thingsdb,json_response
arr = ['a', 'b', 'c'];

arr.clear();
arr;  // the list is empty
```

> Return value in JSON format

```json
[]
```
