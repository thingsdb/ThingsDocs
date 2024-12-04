---
title: "name"
weight: 113
---

Returns the name of the room or [nil](../../nil) if the room is nameless.

This function does *not* generate a [change](../../../overview/changes).

### Function

*room*.`name()`

### Arguments

None

### Return value

Returns the name of the room or `nil`.

### Example

> This code creates a room, gives the room a name and uses the _name()_ function to return the name.

```thingsdb,json_response
.room = room();
.room.set_name('my_room');

// Return the name
.room.name();
```

> Return value in JSON format

```json
"my_room"
```
