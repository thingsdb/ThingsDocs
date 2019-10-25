---
title: "len"
date: 2019-10-23T13:54:12+02:00
draft: true
---

Returns the length of an [list](../../list), [tuple](../../tuple) or [string](../../str), or the number of items in a [thing](../../thing).

This function does *not* generate an [event](../../../events).

### Function
*iterable*.`len()`

### Arguments
None

### Return value
Returns length of the iterable.

> This code uses `len()` to return the number of items in a collection:

```thingsdb,json_response
[1, 2, 3, 4].len();
```

> Return value in JSON format

```json
4
```
