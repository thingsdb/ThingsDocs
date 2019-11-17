---
title: "sort"
weight: 36
---

When this method is used on an [list](..) or [tuple](../../tuple), a new sorted list is returned.

This function does *not* generate an [event](../../../events).

### Function

*array*.`sort([closure, [reverse]])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (optional) | Closure to execute on each value, which is used to determine how the list should be sorted.
reverse | bool (optional) | Determines the order of the returned list.

{{% notice note %}}
The *reverse* argument cannot be used together with a closure which takes two arguments. In this case the order should be specified within the closure.
{{% /notice %}}

### Return value

A new sorted list.


> Simple sort

```thingsdb,json_response
// return a new list in ascending order
[3, 1, 2].sort();
```

> Return value in JSON format

```json
[
    1,
    2,
    3
]
```

> Reverse sort

```thingsdb,json_response
// return a new list in descending order
[3, 1, 2].sort(true);
```

> Return value in JSON format

```json
[
    3,
    2,
    1
]
```

> Sort using a one-argument callback

```thingsdb,json_response
// return a new list in ascending order, case-insensitive
["charlie", "alpha", "Beta"].sort(|s| s.lower());
```

> Return value in JSON format

```json
[
    "alpha",
    "Beta",
    "charlie"
]
```

> Sort using a two-argument callback

```thingsdb,json_response
// list with `nil` values
arr = [nil, "charlie", nil, "alpha", "beta"];

// return a new list in ascending order with `nil` values last
arr.sort(|a, b| isnil(a) ? 1 : isnil(b) ? -1 : a < b ? -1 : a > b ? 1 : 0);
```

> Return value in JSON format

```json
[
    "alpha",
    "beta",
    "charlie",
    null,
    null
]
```

