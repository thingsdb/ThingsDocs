---
title: "cos"
weight: 259
---

Return the cosine of a given number. The value passed in this function should be in radians.

This function does *not* generate a [change](../../../overview/changes).

### Function

`cos(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number

### Return value

Returns with a [float](../../../data-types/float), the cosine of value passed as argument.

### Example

> _cos()_ function example:

```thingsdb,json_response
`The value of cosine of pi / 3 is {cos(MATH_PI / 3)}`
```

> Return value in JSON format

```json
"The value of cosine of pi / 3 is 0.5"
```
