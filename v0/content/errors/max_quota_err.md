---
title: "max_quota_err"
weight: 314
---

Returns an [error](../../data-types/error) when a quota limit is reached.

This function does *not* generate an [event](../../overview/events).

### Function

`max_quota_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value.

### Example

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
