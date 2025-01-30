---
title: "remove"
weight: 179
---

This function removes all properties from a [thing](../../thing) that satisfies the callback function.
The removed *values* will be returned in a new list. An empty list is returned if no values are removed.

This function generates a [change](../../../overview/changes).

### Function

*thing*.`remove(callback, [limit])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.
limit    | int (optional) | Limit the number of properties to remove.

Explanation of the *callback* argument:

Iterable | Arguments | Description
-------- | -------- | -----------
thing | key, value | Iterate over properties of the thing. Both key and value are optional.

{{% notice warning %}}
If a callback satisfies more than a given `limit` of properties, it is not reliable *which* properties are removed as the order of properties on a thing is not guaranteed.
{{% /notice %}}

### Return value

A list with the values from the removed properties.

### Example

> This code shows an example using ***remove()*** on a thing:

```thingsdb,json_response
tmp = {
    a: 1,
    b: 2,
    c: 3,
    d: 4
};

// Return the removed values and tmp with the remaining properties
[
    tmp.remove(|k, v| v%2==0),
    tmp,
];
```

> Return value in JSON format

```json
[
    [
        2,
        4
    ],
    {
        "a": 1,
        "c": 3
    }
]
```