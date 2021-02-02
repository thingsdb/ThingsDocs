---
title: "sort"
weight: 80
---

When this function is used on a [list](..) or [tuple](../../tuple), a new sorted list is returned.

This function does *not* generate an [event](../../../overview/events).

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

### Examples

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

With the `reverse` argument set to `true`, a new list will be returned in descending order.

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

When using a [closure](../../closure) the sort behavior depends on the number of arguments the closure accepts.
With *one* argument, each item in the list will be passed to the closure and the *return* value of the closure will be
used to compare. Below is an example which uses such a closure to do a case-insensitive sort. Another common use
case is when you want to sort [things](../../thing) based on a property. For example a closure like `|u| u.age`
could be used to sort users based on an `age` property.

> Sort using an one-argument callback

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

As a second option the sort function can accept a closure with two arguments. The return value of the given closure
must return an [integer](../../int) value. When this value is `< 0` then `a` goes before `b`, when `0` then both `a` and `b` are considered equal, and when `>0` then `a` goes after `b`.

> Sort using a two-argument callback

```thingsdb,json_response
// list with `nil` values
arr = [nil, "charlie", nil, "alpha", "beta"];

// return a new list in ascending order with `nil` values at the end
arr.sort(|a, b| is_nil(a) ? 1 : is_nil(b) ? -1 : a < b ? -1 : a > b ? 1 : 0);
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
