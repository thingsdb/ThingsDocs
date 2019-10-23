---
title: "map"
date: 2019-10-23T13:52:38+02:00
weight: 5
---

Iterate over items in an [list](../../list), [tuple](../../tuple), [set](..) or over all properties on a [thing](../../thing).

{{% notice warning %}}
Be aware that the order when iterating over a *set* or a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate an [event](../../../events).

### Function
*iterable*.`map(callback)`

### Arguments
Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both item and index are optional.
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.
thing    | name, value | Iterate over the thing properties. Both name and value are optional.

### Return value
A new array with each element being the result of the callback function.

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
