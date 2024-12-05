---
title: "Example emit"
weight: 23
---

Emit an event to a room in a collection.  A successful emit request will respond with `OK (17)`

> Syntax

```none
[scope, room_id, event, ...args]
```

The `room_id` parameter accepts either a *room*-ID or *room*-name to designate the desired room.

{{% notice note %}}
Room names require ThingsDB version **1.7.0** or higher.
{{% /notice %}}

The `args` are optional argument to send with the event.

{{% notice warning %}}
The socket needs to be authorized before sending a `emit` request.
See the [auth example](../auth) for how to authorize a socket connection.
{{% /notice %}}

## Example

As an example we assume that we have a room with Id 17 in collection *stuff*.

This is the data we want to pack *(emit event "new-message" to room Id 17 with one argument "Hello!")*:

`["//stuff", 17, "new-message", "Hello!"]`

Serializing the above using [MessagePack](https://msgpack.org) results in the following `29` bytes:

`\x94\xa7//stuff\x11\xabnew-message\xa6Hello!`

Now we create the header. For this example we just use Id 0:

- Data length (29) `\x1d\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Request Emit package type (40) `\x28`
- Inverse type check bit (247) `0xd7`

> Sending the *Emit* package

```none
\x1d\x00\x00\x00\x00\x00\x28\xd7\x94\xa7//stuff\x11\xabnew-message\xa6Hello!
```

> Responding *OK* package

```none
\x00\x00\x00\x00\x00\x00\x11\xee
```