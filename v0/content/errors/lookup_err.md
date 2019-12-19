---
title: "lookup_err"
weight: 187
---

Returns an [error](../../data-types/error) when a requested resource is not found or when an index is out-of-range.

This function does *not* generate an [event](../../overview/events).

### Function
`lookup_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

### Example

> This code shows ***lookup_err()***:

```thingsdb,json_response
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
