---
title: "auth_err"
date: 2019-10-14T10:11:22+02:00
weight: 2
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`auth_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***auth_err()***:

```thingsdb,json_response
auth_err();
```

> Return value in JSON format

```json
{
    "!": "auth_err()",
    "error_code": -56,
    "error_msg": "authentication error"
}
```
