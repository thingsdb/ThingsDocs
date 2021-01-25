---
title: "cancelled_err"
weight: 296
---

Returns an [error](../../data-types/error) when an operation is cancelled before completion. Fox example by a time-out or stop of service.

This function does *not* generate an [event](../../overview/events).

### Function

`cancelled_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value.

### Example

> This code shows ***cancelled_err()***:

```thingsdb,json_response
cancelled_err();
```

> Return value in JSON format

```json
{
    "!": "cancelled_err()",
    "error_code": -64,
    "error_msg": "operation is cancelled before completion"
}
```
