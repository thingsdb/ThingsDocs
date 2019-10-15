---
title: "num_arguments_err"
date: 2019-10-14T10:12:52+02:00
weight: 8
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`num_arguments_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***num_arguments_err()***:

```
num_arguments_err();
```

> Return value in JSON format

```json
{
    "!": "num_arguments_err()",
    "error_code": -62,
    "error_msg": "wrong number of arguments"
}
```
