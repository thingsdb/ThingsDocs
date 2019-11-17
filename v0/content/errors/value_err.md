---
title: "value_err"
weight: 119
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`value_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***value_err()***:

```thingsdb,json_response
value_err();
```

> Return value in JSON format

```json
{
    "!": "value_err()",
    "error_code": -60,
    "error_msg": "object has the right type but an inappropriate value"
}
```
