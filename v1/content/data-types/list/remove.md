---
title: "remove"
weight: 79
---

This function removes all values in the [list](../../list) that satisfies the callback function.
The removed values will be returned in a new list. An empty list is returned if no values are removed.

This function generates a [change](../../../overview/changes).

### Function

*list*.`remove(callback, [limit])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.
limit    | int (optional) | Limit the number of items to remove. When negative, removal starts at the end of the list and removes at most the absolute value of *limit*.

Explanation of the *callback* argument:

Iterable | Arguments | Description
-------- | -------- | -----------
list | item, index | Iterate over items in the list. Both item and index are optional.

{{% notice note %}}
When `limit` is a negative value, removing starts at the end of the list. Note that in this case the returned *list* still contains the removed items in the same order as they were in the original *list*.
{{% /notice %}}

### Return value

A list with the removed items from the list. The order of items in the new list will be the same as the original order in the list.

### Example

> This code shows an example using ***remove()*** on a list:

```thingsdb,json_response
tmp = [1, 2, 3, 4];
[
    tmp.remove(|x| x%2==0),
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

> Example with a negative limit:

```thingsdb,json_response
tmp = [1, 2, 3, 4, 5, 6, 7, 8];

// Remove the last two items from the list which pass the test
[
    tmp.remove(|x| x%2==0, -2),
    tmp,
];
```

> Return value in JSON format *(note that the order is equal to the original list)*

```json
[
    [
        6,
        8
    ],
    [
        1,
        2,
        3,
        4,
        5,
        7
    ]
]
```
