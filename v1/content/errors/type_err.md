---
title: "type_err"
weight: 325
---

Returns an [error](../../data-types/error) when a given value is of the incorrect type.

This function does *not* generate a [change](../../overview/changes).

### Function

`type_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value.

### Example

> This code shows ***type_err()***:

```thingsdb,json_response
type_err();
```

> Return value in JSON format

```json
{
    "!": "type_err()",
    "error_code": -61,
    "error_msg": "object of inappropriate type"
}
```
