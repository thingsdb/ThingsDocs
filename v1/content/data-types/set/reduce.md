---
title: "reduce"
weight: 129
---

Executes a given reducer [closure](../../closure) on every thing in the set, accumulating to a single return value.

{{% notice warning %}}
A set is **unordered** and therefore the order how things are processed by the reducer might be different from what you expect.
{{% /notice %}}

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`reduce(reducer, [initial])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
reducer | closure (required) | Closure to execute on every thing (except for the first, if no initial value is provided).
initial | any (optional) | The initial value serves as the first argument of the callback during the first call. If no initial value is provided, the first thing in the set will be used instead and not processed by the callback. Calling reduce() on an empty set without an initial value will raise a [lookup_err()](../../../errors/lookup_err).

The *reducer* argument takes three optional arguments:

Argument | Description
-------- | -----------
`(0)` accumulator | An accumulated value that is returned by the previously invoked callback—or initial value.
`(1)` current | The current thing in the set that is being processed by the callback.
`(2)` Id | Id of the current thing in the set that is being processed by the callback.

### Return value

The single value that results from the reduction.

### Examples

> Sum all the values of a list:

```thingsdb,json_response
users = set({
    name: 'Iris',
    age: 7,
}, {
    name: 'Tess',
    age: 6
});

users.reduce(|total, user| total + user.age, 0);
```

> Return value in JSON format

```json
13
```
