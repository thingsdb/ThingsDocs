---
title: "len"
date: 2019-10-23T13:54:12+02:00
weight: 7
---

Returns the length of a [set](..).

This function does *not* generate an [event](../../../events).

### Function

*set*.`len()`

### Arguments

None

### Return value

Returns length of the set.

> This code uses `len()` to return the number of items in a set:

```thingsdb,json_response
set([1, 2, 3, 4]).len();
```

> Return value in JSON format

```json
4
```
