---
title: "len"
date: 2019-10-23T12:51:58+02:00
weight: 6
---

Returns the length of a [list](..) or [tuple](../../tuple).

This function does *not* generate an [event](../../../events).

### Function

*array*.`len()`

### Arguments

None

### Return value

Returns length of the array.

> This code uses `len()` to return the number of items in a collection:

```thingsdb,json_response
[1, 2, 3, 4].len();
```

> Return value in JSON format

```json
4
```
