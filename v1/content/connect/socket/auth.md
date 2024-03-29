---
title: "Example auth"
weight: 16
---

Used for authorizing the socket connection. A successful authentication will respond with `OK (17)`

Authorization can be done by using either a username and password combination or by a token.

> Syntax username/password

```none
[username, password]
```

> Syntax token

```none
"token_string"
```

## Example username/password

As an example we create an authentication package for the default *admin* user with password *pass*.

This is the package data for our authentication request:

`["admin", "pass"]`

Serializing the above using [MessagePack](https://msgpack.org) results in the following `12` bytes:

`\x92\xa5admin\xa4pass`

Now we create the header. For this example we just use Id 0:

- Data length (12) `\x0c\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Auth package type (33) `\x21`
- Inverse type check bit (222) `\xde`

> Sending the *Auth* package

```none
\x0c\x00\x00\x00\x00\x00\x21\xde\x92\xa5admin\xa4pass
```

> Responding *OK* package

```none
\x00\x00\x00\x00\x00\x00\x11\xee
```

## Example token

First, a token is required and can be created using the [new_token()](../../../thingsdb-api/new_token) function.

Suppose our token is `RzDFlsoucQfDqrwrfGGEtc`.

Serializing the token using [MessagePack](https://msgpack.org) results in the following `23` bytes:

`\xb6RzDFlsoucQfDqrwrfGGEtc`

Now we create the header. For this example we just use Id 0:

- Data length (23) `\x17\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Auth package type (33) `\x21`
- Inverse type check bit (222) `\xde`

> Sending the *Auth* package

```none
\x17\x00\x00\x00\x00\x00\x21\xde\xb6RzDFlsoucQfDqrwrfGGEtc
```

> Responding *OK* package

```none
\x00\x00\x00\x00\x00\x00\x11\xee
```