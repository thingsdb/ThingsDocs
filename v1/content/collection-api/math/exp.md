---
title: "exp"
weight: 270
---

Returns _e_ raised to the power of _x_.

The number _e_ is the base of the natural system of logarithms _(defined as `MATH_E`, approximately 2.718282)_ and _x_ is the number passed to the function.

This function does *not* generate a [change](../../../overview/changes).

### Function

`exp(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number

### Return value

Returns with a [float](../../../data-types/float) value.

### Example

> _cos()_ function example:

```thingsdb,json_response
exp(12);
```

> Return value in JSON format

```json
162754.79141900392
```
