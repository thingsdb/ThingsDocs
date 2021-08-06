---
title: "bool"
weight: 30
---

Booleans are either `true` or `false`.
Other types can convert to `bool` by using the `!` (not) operator or the [bool](../../collection-api/bool) function.

> This code creates a *bool* property *is_the_earth_flat* to collection *stuff*:

```thingsdb,should_pass
.is_the_earth_flat = !true;
```

### Related functions

Function | Description
------ | -----------
[bool](../../collection-api/bool) | Create a new boolean value.
[is_bool](../../collection-api/is_bool) | Test if a given value is of type bool.
