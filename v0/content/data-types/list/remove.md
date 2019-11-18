---
title: "remove"
weight: 35
---

This function removes and returns the value of the *first* element in the [list](../../list) that satisfies the callback function.
Otherwise `nil` is returned unless an alternative return value is specified.

This function generates an [event](../../../events).

### Function

*list*.`remove(callback, [alt])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each value until the closure evaluates to true.
alt | any (optional) | Alternative value which is returned if no item has passed the *callback* test.

Explanation of the *callback* argument:

Iterable | Arguments | Description
-------- | -------- | -----------
list | item, index | Iterate over items in the list. Both item and index are optional.

{{% notice note %}}
The `alt` argument will be *lazy* evaluated. Consider the following example: \
`elems.remove(|e| (e.name == "foo"), items.pop());` \
Here, the item will *only* be popped, in case `e` with `name` *foo* is *not* found in `elems`.
{{% /notice %}}

### Return value

The value of the first element in the list that satisfies the provided testing function;
otherwise, `nil` or a specified alternative value is returned.

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
    2,
    [
        1,
        3,
        4
    ]
]
```
