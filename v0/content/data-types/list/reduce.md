---
title: "reduce"
weight: 76
---

Executes a given reducer [closure](../../closure) on every item of the list, accumulating to a single return value.

This function does *not* generate an [event](../../../overview/events).

### Function

*array*.`reduce(reducer, [initial])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
reducer | closure (required) | Closure to execute on every value (except for the first, if no initial value is provided).
initial | any (optional) | The initial value serves as the first argument of the callback during the first call. If no initial value is provided, the first item in the array will be used instead and not processed by the callback. Calling reduce() on an empty list without an initial value will raise a [lookup_err()](../../../errors/lookup_err).

The *reducer* argument takes three optional arguments:

Argument | Description
-------- | -----------
`(0)` accumulator | An accumulated value that is returned by the previously invoked callback—or initial value.
`(1)` current | The current item in the list that is being processed by the callback.
`(2)` index | The index of the current item in the list that is being processed by the callback. If an initial value is given, it start from index `0`, else, it starts from index `1`.

### Return value

The single value that results from the reduction.

### Examples

> Sum all the values of a list:

```thingsdb,json_response
[0, 1, 2, 3].reduce(|a, b| a+b);
```

> Return value in JSON format

```json
6
```

> Sum values in a thing list:

```thingsdb,json_response
// An initial value is required
[{x: 1}, {x: 2}, {x: 3}].reduce(|a, b| a+b.x, 0);
```

> Return value in JSON format

```json
6
```

> Flatten a list with tuples:

```thingsdb,json_response
// Use an empty list as initial value
[[1, 2], [3, 4], [5, 6]].reduce(|a, b| {a.extend(b); a}, []);
```

> Return value in JSON format

```json
[1, 2, 3, 4, 5, 6]
```
