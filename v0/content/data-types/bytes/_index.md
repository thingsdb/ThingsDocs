---
title: "bytes"
weight: 20
---

The bytes type can be used to store a sequence of byte values.

> This code converts a string to bytes

```thingsdb,should_pass
.as_bytes = bytes("Hello ThingsDB!");
```

### Methods

Method | Description
------ | -----------
[len](./len) | Returns the length of the byte sequence.

### Related functions

Method | Description
------ | -----------
[bytes](../../collection-api/bytes) | Create a new bytes value.
[isbytes](../../collection-api/isbytes) | Test if a given value is of type bytes.
