---
title: "Floating point"
date: 2019-10-14T09:40:47+02:00
weight: 5
---

ThingsDB uses 64bit to store float values and has support for the `e` notation and
special *float* values like `inf`, `-inf` and `nan`.

### Useful methods

Method | Description
------ | -----------
[float](../../collection-api/float) | return a float type for a given value.
[isfloat](../../collection-api/isfloat) | check if the given value is of the float type.
[isinf](../../collection-api/isinf) | check if the given value is infinite.
[isnan](../../collection-api/isnan) | check if the given value is not-a-number.

> This code creates a *float* property *plank_constant* to collection *stuff*:

```thingsdb,should_pass
// Assign property `plank_constant`
.plank_constant = 6.62607004e-34;
```
