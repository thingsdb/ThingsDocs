---
title: "bool"
date: 2019-10-14T09:40:19+02:00
weight: 100
---

Booleans are either `true` or `false`.
Other types can convert to `bool` by using the `!` (not) operator or the [bool](../../collection-api/bool) function.

> This code creates a *bool* property *is_the_earth_flat* to collection *stuff*:

```thingsdb,should_pass
.is_the_earth_flat = !true;
```


### Related functions

Method | Description
------ | -----------
[bool](../../collection-api/bool) | Create a new boolean value.
[isbool](../../collection-api/isbool) | Test if a given value is of type bool.