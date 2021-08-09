---
title: "id"
weight: 92
---

Returns the `id` of a [room](..) or `nil` if the room is not stored.

This function does *not* generate a [change](../../../overview/changes).

### Function

*room*.`id()`

### Arguments

None

### Return value

Returns `id` of a room or `nil` when the room is not stored.

### Example

> This code uses `id()` to return a collection id:

```thingsdb,should_pass
.chat = room();
.chat.id();  // Returns the collection id
```

> Example return value in JSON format

```json
624
```
