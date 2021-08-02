---
title: "Listening"
weight: 306
chapter: false
---

Socket connections can listen to events from ThingsDB. It is not possible to listen to events the HTTP API.

The following events may be received by a client:

Event | Description
------------ | -----------
[NODE_STATUS](./node-status) (`0`) | The connected node has changed its status.
[WARNING](./warning) (`5`) | A warning message from ThingsDB.
[ON_JOIN](./on-join) (`6`) | Emitted when a room is joined.
[ON_LEAVE](./on-leave) (`7`) | Emitted when leaving a room *(only when explicitly leaving a room, not on a client disconnect)*.
[ON_EMIT](./on-emit) (`8`) | a *change* is emitted to this room.
[ON_DELETE](./on-delete) (`9`) | A joined [room](../data-types/room) is removed from ThingsDB.

> The number `0-9` represents the package type in a [package header](http://localhost:1313/v0/connect/socket/#package).

## Node status changes and warnings

When connected and authenticated with a socket connection, you will automatically receive *[node-status-changes]((./node-status)* and *[warning-events](./warning)*.

## Join rooms

When joining one or more rooms, ThingsDB is guaranteed to return with the response on the join request before the *[on_join](./on-join)* events are being transmitted.
The *[on_leave](./on-leave)* event is only transmitted when an explicit request is made to leave a room. Thus, this event is *not* triggered when a client disconnect, or when a node is shutting down.
