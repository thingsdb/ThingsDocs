---
title: "Socket"
weight: 17
---

This is a more in depth view of the socket protocol used for communication with ThingsDB.
In case you just want to use ThingsDB using one of the language bindings, then this
info can be skipped. If you plan to implement your own connector, then this info might
be useful to you.

This section applies to communication with ThingsDB over a socket, either by using TCP or a UNIX PIPE connection.
Once a connection is made, packages can be send to ThingsDB. Each package starts
with a 8 bytes header using little endian, followed by optional data. Before you can
send queries to ThingsDB, the connection must be authenticated. This can be done by
sending an `AUTH` package.

## Package

#### LEN (Unsigned, 32bit)

Length of the *data*, stored as **Unsigned, 32-bit, Little Endian**. The header size is *not* included in the length.

#### ID (16bit)

The `ID` is a unique identifier assigned to your package by ThingsDB. It allows you to easily map responses to their corresponding requests,
especially when sending multiple requests concurrently. This identifier is a 16-bit integer, ideally stored in little-endian format for consistency.
While using an **unsigned integer is recommended**, signed values can also be used.

#### TYPE (Unsigned, 8bit)

Package type is used to describe what kind of package is transmitted.

#### Request type

Type      | Number | Description
----------| -----| -----------
`PING`    | 32 | Ping, useful as keep-alive.
`AUTH`    | 33 | Authorization., expects: `[username, password]` or a `token_string`.
`QUERY`   | 34 | Query ThingsDB.
`RUN`     | 37 | Run a procedure, see [procedures](../../procedures-api) for more info.
`JOIN`    | 38 | Join one or more room(s).
`LEAVE`   | 39 | Leave one or more room(s).
`EMIT`    | 40 | Emit an event to a room.

##### CHK (Unsigned, 8bit)

Inverse of the type: `type ^ 0xff`. This is used as a check-bit.

#### DATA

Data serialized using [MessagePack](https://msgpack.org).

> Package format:

```none
┌───────────┬───────────┬───────────┬───────────┬───────────┐
│ LEN (4)   │ ID (2)    │ TYPE (1)  │ CHK (1)   │ DATA (..) │
└───────────┴───────────┴───────────┴───────────┴───────────┘
```

## Response type

ThingsDB can respond with one of the following response type:

Type | Number | Description
--------| -----| -----------
`PONG`  | 16 | Success response to `PING` (header only).
`OK`    | 17 | Success response to `AUTH` and `EMIT` (header only).
`DATA`  | 18 | Success response to `QUERY`, `RUN`, `JOIN` and `LEAVE` (with data).
`ERROR` | 19 | Error response (with data).

## Example

As an example we create an authentication package for the default *admin* user with password *pass*.

This is the package data for our authentication request:

`["admin", "pass"]`

Serializing the above using [MessagePack](https://msgpack.org) results in the following `12` bytes:

`\x92\xa5admin\xa4pass`

Now we create the header. For this example we just use ID 0:

- Data length (12) `\x0c\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Auth package type (33) `\x21`
- Inverse type check bit (222) `\xde`

So our total package will be:

`\x0c\x00\x00\x00\x00\x00\x21\xde\x92\xa5admin\xa4pass`

## More examples

Some more examples:

- [sending a ping request](./ping)
- [sending an authentication request](./auth)
- [sending a query request](./query)
- [sending a run request](./run)
- [sending a join request](./join)
- [sending a leave request](./leave)
- [sending an emit event request](./emit)
- [receiving an error response](./error-response)
