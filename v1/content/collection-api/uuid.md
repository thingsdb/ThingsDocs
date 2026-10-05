---
title: "uuid"
weight: 353
---

Returns a new [uuid](../../data-types/uuid) _(version 7)_ or converts a byte sequence or string into a UUID.

When a string is provided, it may contain lowercase or uppercase characters, and hyphens are optional.

This function does *not* generate a [change](../../overview/changes).

### Function

`uuid([value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | bytes/str (optional) | The value to convert into a UUID.

### Return value

A UUID value. In a client response, the UUID is returned as a lowercase, hyphenated string.

### Example

> This code shows how to create UUIDs:

```thingsdb,should_pass
[
    uuid(),  // new random UUID (version 7)
    uuid('01a08b43-4abd-7529-82a2-9ae352b2f10f'),
    uuid('01A08B434ABD752982A29AE352B2F10F'),
];
```

> Example return value in JSON format

```json
[
    "01a0fc69-1f0f-72ef-a2af-ca8afd7822db",
    "01a08b43-4abd-7529-82a2-9ae352b2f10f",
    "01a08b43-4abd-7529-82a2-9ae352b2f10f"
]
```
