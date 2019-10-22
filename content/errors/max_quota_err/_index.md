---
title: "max_quota_err"
date: 2019-10-14T10:12:08+02:00
weight: 6
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`max_quota_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

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
