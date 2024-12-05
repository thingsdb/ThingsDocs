---
title: "set_name"
weight: 115
---

Set the _name_ of a room. Provide a `nil` argument to remove the current name.

This function generates a [change](../../overview/changes).

### Function

*room*.`set_name(name_or_nil)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`name_or_nil` | str/nil (required) | Name for the room or `nil` to remove the name.

### Return value

The value `nil`.

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
