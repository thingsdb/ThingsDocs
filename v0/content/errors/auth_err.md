---
title: "auth_err"
weight: 226
---

Returns an [error](../../data-types/error) when authentication has failed.

This function does *not* generate an [event](../../overview/events).

### Function

`auth_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value.

### Example

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
