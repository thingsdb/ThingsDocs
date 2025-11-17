---
title: "Example leave"
weight: 24
---

Leave one- or more joined rooms. A successful leave request will respond with an array of equal length of the number of rooms.


> Syntax

```none
[scope, ...IDs]
```

The `IDs` parameter accepts either *room*-IDs or *room*-names to designate the desired rooms for leaving.

{{% notice note %}}
Room names require ThingsDB version **1.7.0** or higher.
{{% /notice %}}

{{% notice warning %}}
The socket needs to be authorized before sending a `leave` request.
See the [auth example](../auth) for how to authorize a socket connection.
{{% /notice %}}

## Example

As an example we assume that we want to leave a joined room with Id 17. Instead of a single ID, we could add as much IDs as we wanted. As an example we also add room Id 456 which does not exist in our collection.

This is the data we want to pack *(leave room Ids 17 (exists in out collection) and 456 (does not exist))*:

`["//stuff", 17, 456]`

Serializing the above using [MessagePack](https://msgpack.org) results in the following `13` bytes:

`\x93\xa7//stuff\x11\xcd\x01\xc8`

Now we create the header. For this example we just use Id 0:

- Data length (13) `\x0d\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Request Leave package type (39) `\x27`
- Inverse type check bit (249) `0xd9`

> Sending the *Join* package

```none
\x0d\x00\x00\x00\x00\x00\x27\xd9\x93\xa7//stuff\x11\xcd\x01\xc8
```

> Responding *[17, nil]* package (room Id 17 is found, the second (456) was not)

```none
\x03\x00\x00\x00\x00\x00\x12\xed\x92\x11\xc0
```

A few seconds (or less) later, you will receive a [on-leave](../../../listening/on-leave) event on the socket connection for every room.

See the [listening documentation](../../../listening) for more information.

> Responding *{id: 17}* package for room 17 which was joined in our example:

```none
\x05\x00\x00\x00\xff\xff\x07\xf9\x81\xa2id\x11
```