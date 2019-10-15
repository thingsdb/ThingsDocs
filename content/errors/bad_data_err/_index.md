---
title: "bad_data_err"
date: 2019-10-14T10:11:34+02:00
weight: 3
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`bad_data_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***bad_data_err()***:

```
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
