---
title: "forbidden_err"
weight: 203
---

Returns an [error](../../data-types/error) when the client or user is missing the required privileges.

This function does *not* generate an [event](../../overview/events).

### Function
`forbidden_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

### Example

> This code shows ***forbidden_err()***:

```thingsdb,json_response
forbidden_err();
```

> Return value in JSON format

```json
{
    "!": "forbidden_err()",
    "error_code": -55,
    "error_msg": "forbidden (access denied)"
}
```
