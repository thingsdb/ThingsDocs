---
title: "bytes"
weight: 30
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
[bytes](../../collection-api/bytes) | Create a new bytes value.
[is_bytes](../../collection-api/is_bytes) | Test if a given value is of type bytes.
