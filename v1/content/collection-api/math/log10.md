---
title: "log10"
weight: 274
---

Return the base 10 logarithm of a given number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`log10(number)`

### Arguments

Argument | Type                 | Description
-------- | -------------------- | ------------
number   | int/float (required) | Input number, must be > 0.

### Return value

Returns with a [float](../../../data-types/float) or a [value_err()](../../../errors/value_err) on negative or zero input number.

### Example

> _log10()_ function example:

```thingsdb,json_response
log10(2.7183);
```

> Return value in JSON format

```json
0.43429738512450866
```
