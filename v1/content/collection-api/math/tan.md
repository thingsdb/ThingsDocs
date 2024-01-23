---
title: "tan"
weight: 269
---

Return the tangent of a given number. The value passed in this function should be in radians.

This function does *not* generate a [change](../../../overview/changes).

### Function

`tan(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number

### Return value

Returns with a [float](../../../data-types/float), the tangent of value passed as argument.

### Example

> _tan()_ function example:

```thingsdb,json_response
`The value of tangent of pi / 6 is {tan(MATH_PI / 6)}`
```

> Return value in JSON format

```json
"The value of tangent of pi / 6 is 0.57735"
```
