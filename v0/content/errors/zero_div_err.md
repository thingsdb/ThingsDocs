---
title: "zero_div_err"
weight: 183
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../overview/events).

### Function
`zero_div_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

### Example

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
