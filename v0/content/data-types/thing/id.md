---
title: "id"
weight: 78
---

Returns the `id` of a [thing](..) or `nil` if the thing is not stored.

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`id()`

### Arguments

None

### Return value

Returns `id` of a thing or `nil` when the thing is not stored.

### Example

> This code uses `id()` to return a collection id:

```thingsdb,should_pass
.id();  // Returns the collection id
```

> Example return value in JSON format

```json
3
```
