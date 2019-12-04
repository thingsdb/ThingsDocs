---
title: "value_err"
weight: 187
---

Returns an [error](../../data-types/error) when a given value has the correct type but contains invalid data.

This function does *not* generate an [event](../../overview/events).

### Function
`value_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

### Example

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
