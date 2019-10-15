---
title: "lookup_err"
date: 2019-10-14T10:11:56+02:00
weight: 5
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`lookup_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***lookup_err()***:

```
lookup_err();
```

> Return value in JSON format

```json
{
    "!": "lookup_err()",
    "error_code": -54,
    "error_msg": "requested resource not found"
}
```
