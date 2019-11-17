---
title: "Example"
weight: 1
---

## Example
As an example we create an authentication package for the default *admin* user with password *pass*.

This is the package data for our authentication request:

`["admin", "pass"]`

Serializing the above using *msgpack* results in the following `12` bytes:

`\x92\xa5admin\xa4pass`

Now we create the header, for this example we just use ID 0:

- Data length (12) `\x0c\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Auth package type (33) `\x21`
- Inverse type check bit (222) `\xde`


So our total package will be:

`\x0c\x00\x00\x00\x00\x00\x21\xde\x92\xa5admin\xa4pass`
