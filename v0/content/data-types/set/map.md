---
title: "map"
weight: 46
---

Iterate over items in an [set](..).

{{% notice warning %}}
Be aware that the order when iterating over a *set* or a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate an [event](../../../events).

### Function

*set*.`map(callback)`

### Arguments

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.

### Return value

A new list with each element being the result of the callback function.

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
