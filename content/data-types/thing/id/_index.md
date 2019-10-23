---
title: "id"
date: 2019-10-23T13:54:06+02:00
weight: 5
---

Returns the `id` of a [thing](../../thing) or `nil` if the thing is not stored.

This function does *not* generate an [event](../../../events).

### Function
*thing*.`id()`

### Arguments
None

### Return value
Returns `id` of a thing or `nil` when the thing is not stored.

> This code uses `id()` to return a collection id:

```thingsdb,should_pass
.id();  // Returns the collection id
```

> Example return value in JSON format

```json
3
```
