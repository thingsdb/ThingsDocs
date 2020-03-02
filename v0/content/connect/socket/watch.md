---
title: "Example watch"
weight: 12
---

Subscribe for watching a node or things in ThingsDB. A successful run request will respond with a `OK (17)` package.

> Syntax

```
[scope, ...IDs]
```

The `IDs` are the *thing*-IDs you want to watch.

{{% notice warning %}}
The socket needs to be authorized before sending a `watch` request.
See the [auth example](../auth) for how to authorize a socket connection.
{{% /notice %}}

## Example

As an example we assume that we want to watch a thing with ID 3 for mutations. Instead of a single ID, we could add as much IDs as we wanted.

{{% notice info %}}
ThingsDB will throw a `WARNING` event to you socket connection in case some given ID does not exist within the given collection scope.
Other IDs will be watched and the response to you watch request will still be `OK (17)`.
{{% /notice %}}

This is the data we want to pack:

`["//stuff", 3]`

Serializing the above using [MessagePack](https://msgpack.org) results in the following `10` bytes:

`\x92\xa7//stuff\x03`

Now we create the header. For this example we just use ID 0:

- Data length (13) `\x0a\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Run package type (35) `\x23`
- Inverse type check bit (218) `\xdc`


> Sending the *Query* package

```
\x0a\x00\x00\x00\x00\x00\x23\xdc\x92\xa7//stuff\x03
```

> Responding *OK* package

```
\x00\x00\x00\x00\x00\x00\x11\xee
```

A few seconds (or less) later, you will receive an [init](../../../watching/on-init) or [warning](../../../watching/warning) event on the socket connection.

See the [watching documentation](../../../watching) for more information.

