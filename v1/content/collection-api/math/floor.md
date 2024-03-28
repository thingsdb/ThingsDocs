---
title: "floor"
weight: 263
---

Return the floor of a given number. This is the largest integer <= the given number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`floor(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number

### Return value

Returns with an [int](../../../data-types/int) or an [overflow_err()](../../../errors/overflow_err) when outside the range of `INT_MIN` and `INT_MAX`.

### Example

> _floor()_ function example:

```thingsdb,json_response
floor(4.31);
```

> Return value in JSON format

```json
4
```
