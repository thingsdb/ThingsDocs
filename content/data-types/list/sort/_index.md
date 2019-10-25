---
title: "sort"
date: 2019-10-23T12:52:33+02:00
weight: 11
---

When this method is used on an [list](..) or [tuple](../../tuple), a new sorted list is returned.

### Function

*array*.`sort([closure, [reverse]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (optional) | Closure to execute on each value, which is used to determine how the list should be sorted.
reverse | bool (optional) | Determines the order of the returned list.

{{% notice note %}}
An order cannot be specified with a closure which takes two arguments. In this case the order should be specified within the closure.
{{% /notice %}}

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item1, item2 | Iterate over all items in the array. Argument item2 is is optional and can be used to define the order of the returned list.

### Return value

A new sorted list.

> This code shows an example using ***map()***:

```thingsdb,json_response
values = [5, 3, 8, 1];

values.sort();
```

> Return value in JSON format

```json
[
    1,
    3,
    5,
    8
]
```
