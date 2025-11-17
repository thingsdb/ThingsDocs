---
title: "choice"
weight: 72
---

This function returns a **pseudo-random** item from a [list](..) or [tuple](../../tuple). The array must contain at least one
item, otherwise a [lookup_err()](../../../errors/lookup_err) is raised.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`choice()`

### Arguments

None

### Return value

A pseudo-random item from the array or a [lookup_err()](../../../errors/lookup_err) when empty.

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
