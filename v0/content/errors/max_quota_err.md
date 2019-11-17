---
title: "max_quota_err"
weight: 173
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`max_quota_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***max_quota_err()***:

```thingsdb,json_response
max_quota_err();
```

> Return value in JSON format

```json
{
    "!": "max_quota_err()",
    "error_code": -57,
    "error_msg": "max quota is reached"
}
```
