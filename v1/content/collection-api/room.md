---
title: "room"
weight: 259
---

Returns a [room](../../data-types/room) from a specified value, that may be dynamic. If no value is given, a new room is returned.

This function does *not* generate a [change](../../overview/changes).

### Function

`room([id])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
id | int (optional) | The Id for the room to return.

### Return value

Returns a [room](../../data-types/room).
A [lookup_err()](../../errors/lookup_err) is returned in case a room Id is given which is not found inside the collection.

### Example

> This code shows an example usage of ***room()***:

```thingsdb,should_pass
// Create a room which we can use in the example
id = (.my_room = room()).id();

[
    room(id),
    room(),
];
```

> Example return value in JSON format

```json
[
    "room:18",
    "room:nil"
]
```
