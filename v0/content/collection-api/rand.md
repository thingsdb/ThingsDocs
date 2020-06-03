---
title: "rand"
weight: 160
---

Returns **pseudo-random** number between `0.0` and `1.0`.

{{% notice warning %}}
Do not use **rand()** when the purpose is security related since the linear
congruential algorithms used by this function is too easy to break.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`rand()`

### Arguments

None

### Return value

A pseudo-random [float](../../data-types/float) number between `0.0` and `1.0`.

### Example

> Some examples on how ***raise()*** can be used:

```thingsdb,should_pass
// Return a pseudo-random number between 0.0 and 1.0
rand();
```

Example return value in JSON format:

```json
0.54747654169214726
```
