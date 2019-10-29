---
title: "zero_div_err"
date: 2019-10-14T10:13:56+02:00
weight: 14
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`zero_div_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***zero_div_err()***:

```thingsdb,json_response
zero_div_err();
```

> Return value in JSON format

```json
{
    "!": "zero_div_err()",
    "error_code": -58,
    "error_msg": "division or module by zero"
}
```
