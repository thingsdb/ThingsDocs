---
title: "splice"
weight: 52
---

The `splice()` method changes the contents of an list by removing or replacing
existing elements and/or adding new elements in place.

This function generates an [event](../../../overview/events) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`splice(start, [delete_count, [item1, item2, ..., itemX]])`)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
start | int (required) | Start index in the list. If negative, it will begin that many elements from the end of the list.
delete_count | int (optional) | Number of item to remove from `start`. If `<= 0`, no items will be removed.
item1, item2, ..., itemX | any (optional) | Items to add, beginning from `start`.

### Return value

An list containing the deleted elements. If only one element is removed,
an list of one element is returned. If no elements are removed, an empty list is returned.

### Example

> This code replaces an element in a list at position 2:

```thingsdb,json_response
months = ['Jan', 'Feb', 'April'];
months.splice(2, 1, 'March');       /* Returns: ['April'] */
months;
```

> Return value in JSON format

```json
[
    "Jan",
    "Feb",
    "March"
]
```
