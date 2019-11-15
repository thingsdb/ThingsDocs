---
title: "bytes"
date: 2019-10-23T11:04:12+02:00
weight: 200
---

The bytes type can be used to store a sequence of byte values.

> This code converts a string to bytes

```thingsdb,should_pass
.as_bytes = bytes("Hello ThingsDB!");
```

### Methods

Method | Description
------ | -----------
[len](./len) | Returns the length of the bytes.

### Related functions

Method | Description
------ | -----------
[bytes](../../collection-api/bytes) | Create a new bytes value.
[isbytesl](../../collection-api/isbytes) | Test if a given value is of type bytes.