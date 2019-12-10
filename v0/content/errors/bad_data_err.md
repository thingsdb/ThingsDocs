---
title: "bad_data_err"
weight: 179
---

Returns an [error](../../data-types/error) when a request is malformed.

This function does *not* generate an [event](../../overview/events).

### Function
`bad_data_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

### Example

> This code shows ***bad_data_err()***:

```thingsdb,json_response
bad_data_err();
```

> Return value in JSON format

```json
{
    "!": "bad_data_err()",
    "error_code": -53,
    "error_msg": "unable to handle request due to invalid data"
}
```
