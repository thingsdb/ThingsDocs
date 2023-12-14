---
title: "bool"
weight: 35
---

Booleans are either `true` or `false`.
Other types can convert to `bool` by using the `!` (not) operator or the [bool](../../collection-api/bool) function.

{{% notice tip %}}
The [bool() documentation](../../collection-api/bool) contains a helpful example table to explain how different types are converted to bool.
{{% /notice %}}


> This code creates a *bool* property *is_the_earth_flat* to collection *stuff*:

```thingsdb,should_pass
.is_the_earth_flat = !true;
```

### Related functions

Function | Description
------ | -----------
[bool](../../collection-api/bool) | Convert a value into type bool.
[is_bool](../../collection-api/is/is_bool) | Test if a given value is of type bool.
