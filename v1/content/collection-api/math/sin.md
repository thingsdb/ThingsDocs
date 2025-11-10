---
title: "sin"
weight: 281
---

Return the sine of a given number. The value passed in this function should be in radians.

This function does *not* generate a [change](../../../overview/changes).

### Function

`sin(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number

### Return value

Returns with a [float](../../../data-types/float), the sine of value passed as argument.

### Example

> _sin()_ function example:

```thingsdb,json_response
`The value of sine of pi / 6 is {sin(MATH_PI / 6)}`
```

> Return value in JSON format

```json
"The value of sine of pi / 6 is 0.5"
```
