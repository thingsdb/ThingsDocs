---
title: "map"
weight: 96
---

The function iterates over all properties on a [thing](..) and
returns a new [list](../../list) based on the results of a given callback function.

{{% notice warning %}}
Be aware that the order when iterating over a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`map(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
thing    | name, value | Iterate over the thing properties. Both name and value are optional.

### Return value

A new list of items that are the result of the callback function.

### Example

> This code shows an example using ***map()***:

```thingsdb,json_response
user = {name: "Iris", age: 6};

user.map(|property| property.len());
```

> Return value in JSON format

```json
[
    4,
    3
]
```
