---
title: "Example run"
weight: 22
---

Run a procedure in ThingsDB. A successful run request will respond with a `DATA (18)` package.

> Syntax

```none
[scope, procedure, ...args]
```

The `args` are parsed (and *must* match) to the procedure.

{{% notice warning %}}
The socket needs to be authorized before sending a `run` request.
See the [auth example](../auth) for how to authorize a socket connection.
{{% /notice %}}

## Example

As an example we assume there is a procedure created in the `@thingsdb` scope, called *"add_one"* which just adds one to a given value.
The procedure can be created using `new_procedure('add_one', |x| x + 1);`, see [new_procedure()](../../../procedures-api/new_procedure).

This is the data we want to pack:

`["@t", "add_one", 41]`

Serializing the above using [MessagePack](https://msgpack.org) results in the following `13` bytes:

`\x93\xa2@t\xa7add_one)`

Now we create the header. For this example we just use Id 0:

- Data length (13) `\x0d\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Run package type (37) `\x25`
- Inverse type check bit (218) `\xda`

> Sending the *Query* package

```none
\x0d\x00\x00\x00\x00\x00\x25\xda\x93\xa2@t\xa7add_one)
```

> Responding *Data* package

```none
\x01\x00\x00\x00\x00\x00\x12\xed*
```

We see that the `DATA` response package has a header with attached data of length `1`.

Unpacking the data `*` using [MessagePack](https://msgpack.org) will return the expected value `42` which is the expected result.
