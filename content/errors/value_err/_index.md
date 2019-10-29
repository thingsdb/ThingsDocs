---
title: "value_err"
date: 2019-10-14T10:13:47+02:00
weight: 13
---

Returns an [error](../../data-types/error-type).

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
