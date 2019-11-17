---
title: "map"
weight: 870
---

Iterate over items in an [list](../../list) or [tuple](../../tuple).

This function does *not* generate an [event](../../../events).

### Function

*array*.`map(callback)`

### Arguments

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both item and index are optional.

### Return value

A new list with each element being the result of the callback function.

> This code shows an example using ***map()***:

```thingsdb,json_response
users = [{name: "Iris", age: 6}, {name: "Sasha", age: 34}];

// returns ["Iris", "Sasha"]
users.map(|user| user.name);
```

> Return value in JSON format

```json
[
    "Iris",
    "Sasha"
]
```
