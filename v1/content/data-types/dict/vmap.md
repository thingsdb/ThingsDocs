---
title: "vmap"
weight: 73
---

The function returns a new dict with equal keys but values computed as a result of a given closure callback.

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`vmap(callback)`

### Arguments

| Argument | Type               | Description                       |
| -------- | ------------------ | --------------------------------- |
| callback | closure (required) | Closure to execute on each value. |

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
dict     | value       | Iterate over the dict values.

### Return value

Returns a new dict with equal keys but values as a result of a given closure.

### Example

> This code shows how to use `vmap(..)`:

```thingsdb,json_response
d = dict([
    ["a", 1],
    ["b", 2],
    ["c", 3],
]);
d.vmap(|x| x*x);
```

> Return value in JSON format (Warning: the order is *NOT* guaranteed)

```json
[
    ["a", 1],
    ["b", 4],
    ["c", 9]
]
```
