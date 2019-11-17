---
title: "overflow_err"
weight: 10
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`overflow_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***overflow_err()***:

```thingsdb,json_response
overflow_err();
```

> Return value in JSON format

```json
{
    "!": "overflow_err()",
    "error_code": -59,
    "error_msg": "integer overflow"
}
```
