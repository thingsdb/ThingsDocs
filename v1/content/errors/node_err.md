---
title: "node_err"
weight: 320
---

Returns an [error](../../data-types/error) when a node was not able to handle the request.

This function does *not* generate a [change](../../overview/changes).

### Function

`node_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value.

### Example

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
