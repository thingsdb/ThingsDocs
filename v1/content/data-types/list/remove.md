---
title: "remove"
weight: 77
---

This function removes all values in the [list](../../list) that satisfies the callback function.
The removed values will be returned in a new list. An empty list is returned if no value is removed.

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`remove(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each value.

Explanation of the *callback* argument:

Iterable | Arguments | Description
-------- | -------- | -----------
list | item, index | Iterate over items in the list. Both item and index are optional.

### Return value

A list with the removed items from the list. The order of items in the new list will be the same as the original order in the list.

### Example

> This code shows an example using ***remove()*** on a list:

```thingsdb,json_response
tmp = [1, 2, 3, 4];
[
    tmp.remove(|x| (x % 2 == 0)),
    tmp,
];
```

> Return value in JSON format

```json
[
    [
        2,
        4
    ],
    [
        1,
        3
    ]
]
```
