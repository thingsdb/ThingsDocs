---
title: "choice"
weight: 42
---

This function returns a **pseudo-random** item from a [list](..) or [tuple](../../tuple) . The array must contain at least one
item, otherwise a [lookup_err()](../../../errors/lookup_err) is raised.

This function does *not* generate an [event](../../../overview/events).

### Function

*array*.`choice()`

### Arguments

None

### Return value

A pseudo-random item from the array.

### Example

> This code shows an example using ***choice()***:

```thingsdb,should_pass
// Returns either `a`, `b` or `c`
['a', 'b', 'c'].choice();
```

> Example return value in JSON format

```json
"b"
```
