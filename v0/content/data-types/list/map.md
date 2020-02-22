---
title: "map"
weight: 45
---

Iterate over items in an [list](../../list) or [tuple](../../tuple) and
return a new [list](../../list) based on the results of a given callback function.

This function does *not* generate an [event](../../../overview/events).

### Function

*array*.`map(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.


Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over all items in the array. Both item and index are optional.

### Return value

A new list with each element being the result of the callback function.

### Example

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
