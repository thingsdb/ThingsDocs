---
title: "type_err"
weight: 118
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`type_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***type_err()***:

```thingsdb,json_response
type_err();
```

> Return value in JSON format

```json
{
    "!": "type_err()",
    "error_code": -61,
    "error_msg": "object of inappropriate type"
}
```
