---
title: "Example error response"
weight: 17
---

In this example we perform a [query](../query) request and assume the socket connection is not authenticated yet.
We then look at the error response.

## Example

As an example we will perform a useless query with as code just the simple equation `1 + 1;` and we will use the `@thingsdb` scope to perform the query on.

This is the data we want to pack:

`["@t", "1 + 1;"]`

Serializing the above using [MessagePack](https://msgpack.org) results in the following `11` bytes:

`\x92\xa2@t\xa61 + 1;`

Now we create the header. For this example we just use ID 0:

- Data length (11) `\x0b\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Query package type (34) `\x22`
- Inverse type check bit (221) `\xdd`

> Sending the *Query* package

```none
\x0b\x00\x00\x00\x00\x00\x22\xdd\x92\xa2@t\xa61 + 1;
```

> If the connection is *not* authenticated, this will be the responding *Data* package

```none
8\x00\x00\x00\x00\x00\x13\xec\x82\xaaerror_code\xd0\xc8\xa9error_msg\xbfconnection is not authenticated
```

The first 8 bytes (`8\x00\x00\x00\x00\x00\x13\xec`) contain the header:

- Data length `8\x00\x00\x00` = `56`
- Package ID: `\x00\x00` = `0`
- Type: `\x13` = `19 (ERROR)`
- Check-bit: `\xec` = `236 (19^255)`

We see that the `ERROR` response package data of length `56`.

Unpacking the data `\x82\xaaerror_code\xd0\xc8\xa9error_msg\xbfconnection is not authenticated` using [MessagePack](https://msgpack.org) will return the following in JSON format:

```json
{
    "error_code": -56,
    "error_msg": "connection is not authenticated"
}
```
