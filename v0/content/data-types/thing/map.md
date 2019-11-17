---
title: "map"
weight: 64
---

Iterate over all properties on a [thing](..).

{{% notice warning %}}
Be aware that the order when iterating over a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate an [event](../../../events).

### Function

*thing*.`map(callback)`

### Arguments

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
thing    | name, value | Iterate over the thing properties. Both name and value are optional.

### Return value

A new list with each element being the result of the callback function.

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
