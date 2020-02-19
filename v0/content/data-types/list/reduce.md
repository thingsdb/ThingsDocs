---
title: "reduce"
weight: 47
---

Executes a given reducer [closure](../../closure) on each element of the list, resulting in a single output value.

This function does *not* generate an [event](../../../overview/events).

### Function

*list*.`reduce(reducer, [initial])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
reducer | closure (required) | Closure to execute on each value (except for the first, if no initial value is supplied).
initial | any (optional) | A value to use as the first argument to the first call of the callback. If no initial value is supplied, the first element in the array will be used and skipped. Calling reduce() on an empty array without an initial value will raise a [lookup_err()](../../../errors/lookup_err).


The *reducer* argument takes three optional arguments:

Argument | Description
-------- | -----------
`(0)` accumulator | The accumulator accumulates callback's return values. It is the accumulated value previously returned in the last invocation of the callback—or initialValue.
`(1)` current | The current element being processed in the list.
`(2)` index | The index of the current element being processed in the array. Starts from index `0` if an initial value is provided. Otherwise, it starts from index `1`.

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
