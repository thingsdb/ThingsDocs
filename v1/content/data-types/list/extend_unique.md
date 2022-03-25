---
title: "extend_unique"
weight: 68
---

Adds a [list](..) or [tuple](../../tuple) with items to the end of a [list](..), and returns the new length. Only items which do not have a duplicate in the list will be added.

An item in the list is marked as a duplicate when an item is compared as equal to another item using the `==` operator.

{{% notice info %}}
If the original list contains duplicate items, those items remain untouched. See [example 2](#example-2).
{{% /notice %}}

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`extend_unique(list)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
list | list/tuple | The `list` or `tuple` to extend the `list` with.

### Return value

Returns the new length of the list.

### Example 1

> This code extends a list with a given array:

```thingsdb,json_response
a = [0, 1, 2];
b = range(6);
a.extend_unique(b);  // returns the new length, 6 (0, 1 and 2 are not added again)
a;
```

> Return value in JSON format

```json
[
    0,
    1,
    2,
    3,
    4,
    5
]
```

### Example 2

> Existing duplicates remain untouched:

```thingsdb,json_response
list1 = ['A', 'A', 'B'];
list2 = ['B', 'B', 'C'];
list1.extend_unique(list2);

// Note that list2 is untouched and pre-existing duplicates
// in list1 are not removed
{
    list1: list1,
    list2: list2
};
```

> Return value in JSON format

```json
{
    "list1": [
        "A",
        "A",
        "B",
        "C"
    ],
    "list2": [
        "B",
        "B",
        "C"
    ]
}
```