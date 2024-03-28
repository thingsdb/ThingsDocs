---
title: "each"
weight: 162
---

Iterate over all properties on a [thing](..).

{{% notice warning %}}
Be aware that the order when iterating over a *thing* is not guaranteed.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*thing*.`each(callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
callback | closure (required) | Closure to execute on each value.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
thing    | name, value | Iterate over the thing properties. Both name and value are optional.

### Return value

None

### Example

> This code shows an example using ***each()***:

```thingsdb,json_response
scores = {
    cato: 99,
    iris: 110,
    job: 170,
    sasha: 67,
    tijs: 159,
};

// Just an example, the same could be achieved using `filter` and `map`.
above100 = [];
scores.each(|name, score| score > 100 && above100.push(name) );

// Return all players with a score above 100
above100;
```

> Return value in JSON format

```json
[
    "iris",
    "job",
    "tijs"
]
```
