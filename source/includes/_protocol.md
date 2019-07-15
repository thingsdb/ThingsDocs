
# Protocol
This is a more in depth view of the protocol used for communication with ThingsDB.
In case you just want to use ThingsDB using one of the language bindings, then this
info can be skipped. If you plan to implement you own connector, then this info might
be useful to you.

Communication with ThingsDB is done over a socket, either using TCP or a UNIX PIPE connection.
Once a connection is made, packages can be send to ThingsDB. Each package starts
with a 8 bytes header using little endian, followed by optional data. Before you can
send queries to ThingsDB, the connection must be authenticated. This can be done by
sending an `AUTH` package.

## Package

> Package format:

```
┌───────────┬───────────┬───────────┬───────────┬───────────┐
│ LEN (4)   │ ID (2)    │ TYPE (1)  │ CHK (1)   │ DATA (..) │
└───────────┴───────────┴───────────┴───────────┴───────────┘
```

### LEN (Unsigned, 32bit)
Length of the data, the header not included.

### ID (16bit)
The ID can be used as an identifier of your package. When ThingsDB send a response
on a request, it will use the same ID so this allows you to map a response to a
request. This is useful if you want to send multiple request in parallel.

### TYPE (Unsigned, 8bit)
Package type is used to describe what kind of package is transmitted.

#### Request type
Type | Number | Description
--------| -----| -----------
`PING`  | 32 | Ping, useful as keep-alive.
`AUTH`  | 33 | Authentication, expects: `[username, password]`
`QUERY_COLLECTION` | 36 | Query, see [query](#query) for more info.
`WATCH` | 48 | Watch, see [watch](#watch) for more info.
`UNWATCH` | 49 | Stop watching specified things, see [watch](#watch) for more info.

### CHK (Unsigned, 8bit)
Inverse of the type: `type ^ 0xff`, this is used as a check-bit.

### DATA
Data serialized using [qpack](https://github.com/transceptor-technology/libqpack).

## Example
As an example we create an authentication package for the default *admin* user with password *pass*.

This is the package data for our authentication request:

`["admin", "pass"]`

Serializing the above using *qpack* results in the following `12` bytes:

`\xef\x85admin\x84pass`

Now we create the header, for this example we just use ID 0:

- Data length (12) `\x0c\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Auth package type (33) `\x21`
- Inverse type check bit (222) `\xde`


So our total package will be:

`\x0c\x00\x00\x00\x00\x00\x21\xde\xef\x85admin\x84pass`

