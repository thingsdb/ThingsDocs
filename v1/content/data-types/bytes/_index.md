---
title: "bytes"
weight: 38
---

The bytes type can be used to store a sequence of byte values.

> This code converts a string to bytes

```thingsdb,should_pass
.as_bytes = bytes("Hello ThingsDB!");
```

### Functions

Function | Description
------ | -----------
[len](./len) | Return the length of the byte sequence.

### Related functions

Function | Description
------ | -----------
[base64_decode](../../collection-api/base64_decode) | Decode a Base64 encoded string.
[base64_encode](../../collection-api/base64_encode) | Encode a [bytes](../../data-types/bytes) _(or a [str](../../data-types/str))_ value using Base64.
[bytes](../../collection-api/bytes) | Create a new bytes value.
[is_bytes](../../collection-api/is/is_bytes) | Test if a given value is of type bytes.
