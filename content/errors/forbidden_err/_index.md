---
title: "forbidden_err"
date: 2019-10-14T10:11:45+02:00
weight: 4
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`forbidden_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.

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
