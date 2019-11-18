---
title: "num_arguments_err"
weight: 174
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`num_arguments_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***num_arguments_err()***:

```thingsdb,json_response
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
