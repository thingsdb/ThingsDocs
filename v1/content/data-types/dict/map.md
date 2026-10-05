---
title: "map"
weight: 69
---

The function iterates over all items on a [dict](..) and
returns a new [list](../../list) based on the results of a given callback function.

{{% notice warning %}}
Be aware that the order when iterating over a *set*, *dict* or a *dict* is not guaranteed.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`map(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each key/value pair.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
dict    | key, value | Iterate over the dict items. Both key and value are optional.

### Return value

A new list of items that are the result of the callback function.

### Example

> This code shows an example using ***map()***:

```thingsdb,json_response
d = dict([
    [uuid(), "a"],
    [uuid(), "b"],
    [uuid(), "c"],
]);

d.map(|k, v| v.upper()).sort();
```

> Return value in JSON format

```json
[
    "A",
    "B",
    "C"
]
```
