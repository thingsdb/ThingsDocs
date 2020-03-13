---
title: "Example query"
weight: 14
---

Query ThingsDB. A successful query request will respond with a `DATA (18)` package.

> Syntax

```none
[scope, code, {vars}]
```

The `vars` in the query are optional and may be omitted. When used, `vars` must be a `map` where the `keys`
represent the variable names and the `values` the values for the variable.

{{% notice warning %}}
The socket needs to be authorized before sending a `query` request.
See the [auth example](../auth) for how to authorize a socket connection.
{{% /notice %}}

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

> Responding *Data* package

```none
\x01\x00\x00\x00\x00\x00\x12\xed\x02
```

We see that the `DATA` response package has a header with attached data of length `1`.

Unpacking the data `\x02` using [MessagePack](https://msgpack.org) will return the expected value `2` which is the answer to our equation.

{{% notice warning %}}
If your socket connection is not authenticated then you will receive an [error response](../error-response).
{{% /notice %}}
