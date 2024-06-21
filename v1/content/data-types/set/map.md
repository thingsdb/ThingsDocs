---
title: "map"
weight: 126
---

The function iterates over items in a [set](..) and
returns a new [list](../../list) based on the results of a given callback function.

{{% notice warning %}}
Be aware that the order when iterating over a *set* or a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`map(callback)`

### Arguments

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
set      | thing, Id   | Iterate over things in the set. Both `thing` and `id` are optional.

### Return value

A new list of items that are the result of the callback function.

### Example

> This code shows an example using ***map()***:

```thingsdb,json_response
users = [{name: "Iris", age: 6}, {name: "Sasha", age: 34}];

// returns ["Iris", "Sasha"]
set(users).map(|user| user.name).sort();
```

> Return value in JSON format

```json
[
    "Iris",
    "Sasha"
]
```
