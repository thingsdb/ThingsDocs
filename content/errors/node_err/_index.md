---
title: "node_err"
date: 2019-10-14T10:12:19+02:00
weight: 7
---

Returns an [error](../../data-types/error-type).

This function does *not* generate an [event](../../events).

### Function
`node_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | raw (optional) | Alternative error message.

### Return value
An error value.

> This code shows ***node_err()***:

```thingsdb,json_response
node_err();
```

> Return value in JSON format

```json
{
    "!": "node_err()",
    "error_code": -51,
    "error_msg": "node is temporary unable to handle the request"
}
```
