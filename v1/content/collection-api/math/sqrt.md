---
title: "sqrt"
weight: 270
---

Return the square root of a given number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`sqrt(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number, must be >= 0.

### Return value

Returns with a [float](../../../data-types/float) or a [value_err()](../../../errors/value_err) on negative input number.

### Example

> _sqrt()_ function example:

```thingsdb,json_response
`The square root of 2 is {sqrt(2)}`
```

> Return value in JSON format

```json
"The square root of 2 is 1.41421"
```
