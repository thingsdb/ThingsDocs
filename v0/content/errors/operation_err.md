---
title: "operation_err"
weight: 176
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`operation_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***operation_err()***:

```thingsdb,json_response
operation_err();
```

> Return value in JSON format

```json
{
    "!": "operation_err()",
    "error_code": -63,
    "error_msg": "operation is not valid in the current context"
}
```
