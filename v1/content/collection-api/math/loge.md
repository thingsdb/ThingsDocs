---
title: "loge"
weight: 264
---

Returns the natural logarithm (base _e_) of a given number.

This function does *not* generate a [change](../../../overview/changes).

### Function

`loge(number)`

### Arguments

Argument | Type                 | Description
-------- | ---- ----------------| ------------
number   | int/float (required) | Input number, must be > 0.

### Return value

Returns with a [float](../../../data-types/float) or a [value_err()](../../../errors/value_err) on negative or zero input number.

### Example

> _loge()_ function example:

```thingsdb,json_response
loge(5.6);
```

> Return value in JSON format

```json
1.7227665977411035
```
