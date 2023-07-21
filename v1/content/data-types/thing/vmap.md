---
title: "vmap"
weight: 177
---

The function returns a new thing with equal keys but values computed as a result of a given closure callback.

This function does *not* generate a [change](../../../overview/changes).

### Function

*thing*.`vmap(callback)`

### Arguments

| Argument | Type               | Description                       |
| -------- | ------------------ | --------------------------------- |
| callback | closure (required) | Closure to execute on each value. |

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
thing    | value       | Iterate over the thing values.

### Return value

Returns a new thing with equal keys but values as a result of a given closure.

### Example

> This code shows how to use `vmap(..)`:

```thingsdb,json_response
{a: 1, b: 2, c: 3}.vmap(|x| x*x);
```

> Return value in JSON format

```json
{
    "a": 1,
    "b": 4,
    "c": 9
}
```
