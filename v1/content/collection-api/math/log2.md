---
title: "log2"
weight: 273
---

Return the base 2 logarithm of a given number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`log2(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number, must be > 0.

### Return value

Returns with a [float](../../../data-types/float) or a [value_err()](../../../errors/value_err) on negative or zero input number.

### Example

> _log2()_ function example:

```thingsdb,json_response
log2(2.7183);
```

> Return value in JSON format

```json
1.4427046851812222
```
