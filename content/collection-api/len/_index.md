---
title: "len"
date: 2019-10-14T10:03:17+02:00
weight: 39
---

Returns the length of an [array](../../data-types/array-type) or [string](../../data-types/string-raw), or the number of items in a [thing](../../data-types/thing-type).

This function does *not* generate an [event](../../events).

### Function
*iterable*.`len()`

### Arguments
None

### Return value
Returns length of the iterable.

> This code uses `len()` to return the number of items in a collection:

```
[1, 2, 3, 4].len();
```

> Return value in JSON format

```json
4
```
