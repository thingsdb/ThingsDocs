---
title: "push"
date: 2019-10-23T12:52:17+02:00
weight: 9
---

Adds new items to the end of an array, and returns the new length.

This function generates an [event](../../../events).

### Function
*list*.`push(item1, item2, ..., itemX)`

### Return value
Returns the new length of the list.

> This code pushes values to a list:

```thingsdb,json_response
list = [1, 2, 3];
list.push(4, 5, 6);
```

> Return value in JSON format

```json
6
```
