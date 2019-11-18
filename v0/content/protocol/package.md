---
title: "Package"
weight: 11
---

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
`AUTH`  | 33 | Authentication, expects: `[username, password]` or a `token_string`.
`QUERY` | 34 | Query, see [query](../../query) for more info.
`WATCH` | 35 | Watch, see [watching](../../watching) for more info.
`UNWATCH` | 36 | Stop watching specified things, see [watching](../../watching) for more info.
`RUN` | 37 | Run a procedure, see [procedures](../../procedures-api) for more info.

### CHK (Unsigned, 8bit)
Inverse of the type: `type ^ 0xff`, this is used as a check-bit.

### DATA
Data serialized using [MessagePack](https://msgpack.org).

> Package format:

```
┌───────────┬───────────┬───────────┬───────────┬───────────┐
│ LEN (4)   │ ID (2)    │ TYPE (1)  │ CHK (1)   │ DATA (..) │
└───────────┴───────────┴───────────┴───────────┴───────────┘
```