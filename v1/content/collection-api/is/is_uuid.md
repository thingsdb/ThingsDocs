---
title: "is_uuid"
weight: 272
---

This function determines whether the provided value is a [uuid](../../../data-types/uuid) value or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_uuid(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type uuid, else it returns `false`.

### Example

> This code shows some return values for ***is_uuid()***:

```thingsdb,json_response
[
    is_uuid( uuid() ),
    is_uuid( uuid("01a0fc5d-3fda-7d04-9cb1-27b80f6730b7") ),
    is_uuid( "01a0fc5d-3fda-7d04-9cb1-27b80f6730b7" ),  // str, not a uuid
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false
]
```
