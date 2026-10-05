---
title: "uuid"
weight: 212
---

Universally Unique Identifier type.

{{% notice note %}}
ThingsDB uses **UUID Version 7**, a time-ordered format that combines a Unix millisecond timestamp with random data. This ensures generated UUIDs are naturally sorted by creation time, making them highly efficient for database indexing and sorting.
{{% /notice %}}

> Generate a new unique UUID (version 7):

```thingsdb,should_pass
uuid();  // returns a new UUID (version 7)
```

### Related functions

Function | Description
------ | -----------
[uuid](../../collection-api/uuid) | Create a new UUID from given bytes or a string, or a random UUID (version 7) if no arguments are given.
[is_uuid](../../collection-api/is/is_uuid) | Test if a given value is of type uuid.
