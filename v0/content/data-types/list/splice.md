---
title: "splice"
weight: 80
---

The `splice()` function changes a list by removing or replacing
existing items and/or adding new items.

This function generates an [event](../../../overview/events) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`splice(start, [delete_count, [item1, item2, ..., itemX]])`)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
start | int (required) | Start index in the list. If it is negative, it will start that many items from the end of the list.
delete_count | int (optional) | Number of item to remove from the`start` of the list. If `<= 0`, no items will be removed.
item1, item2, ..., itemX | any (optional) | Items to add, beginning from the `start`of the list.

### Return value

A list containing the deleted items.

### Example

> This code replaces an item in a list at position 2:

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
