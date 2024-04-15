---
title: "Example ping"
weight: 16
---

Can be used as keep-alive. A successful ping will respond with a `PONG (16)`

{{% notice note %}}
No authorization is required for sending a `ping` request.
{{% /notice %}}

## Example

A Ping package has no data so we only need to construct the header:

- Data length (0) `\x00\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Ping package type (32) `\x20`
- Inverse type check bit (223) `\xdf`

> Sending the *Ping* package

```none
\x00\x00\x00\x00\x00\x00\x20\xdf
```

> Responding *Pong* package

```none
\x00\x00\x00\x00\x00\x00\x10\xef
```
