---
title: "abs"
weight: 268
---

Return the absolute value of a given number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`abs(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number

### Return value

Returns with an [int](../../../data-types/int) or [float](../../../data-types/float), depending on the input.

### Example

> _abs()_ function example:

```thingsdb,json_response
`Absolute value of integer is: {abs(-42)}`;
```

> Return value in JSON format

```json
"Absolute value of integer is: 42"
```
