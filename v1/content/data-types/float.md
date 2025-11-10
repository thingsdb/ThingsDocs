---
title: "float"
weight: 64
---

ThingsDB uses 64bit to store float values and has support for the `e` notation and
special *float* values like `inf`, `-inf` and `nan`.

### Useful functions

Function | Description
------ | -----------
[float](../../collection-api/float) | return a float type for a given value.
[is_float](../../collection-api/is/is_float) | check if the given value is of the float type.
[is_inf](../../collection-api/is/is_inf) | check if the given value is infinite.
[is_nan](../../collection-api/is/is_nan) | check if the given value is not-a-number.

> This code creates a *float* property *plank_constant* to collection *stuff*:

```thingsdb,should_pass
// Assign property `plank_constant`
.plank_constant = 6.62607004e-34;
```
