---
title: "push"
weight: 36
---

Adds new items to the end of an list, and returns the new length.

This function generates an [event](../../../overview/events).

### Function

*list*.`push(item1, item2, ..., itemX)`

### Return value

Returns the new length of the list.

### Example

> This code pushes values to a list:

```thingsdb,json_response
list = [1, 2, 3];
list.push(4, 5, 6);
```

> Return value in JSON format

```json
6
```
