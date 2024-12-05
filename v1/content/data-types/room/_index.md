---
title: "room"
weight: 111
---

This type can be used to [emit](./emit) events to all clients which have joined the room.

It is possible to use emit on rooms with Id `nil` but then the event will be emitted to no one.

### Functions

Function | Description
------ | -----------
[emit](./emit) | Emit a *change*.
[id](./id) | Return `id` of the room or `nil` when the room is not stored.
[name](./name) | Return the _name_ of the room or `nil` when the room has no name.
[set_name](./set_name) | Set or remove the _name_ for a room.

