---
title: "overflow_err"
weight: 313
---

Returns an [error](../../data-types/error) when an attempt is made to create an integer value out of the supported 64Bit (signed) range.

This function does *not* generate an [event](../../overview/events).

### Function

`overflow_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value.

### Example

> This code shows ***overflow_err()***:

```thingsdb,json_response
overflow_err();
```

> Return value in JSON format

```json
{
    "!": "overflow_err()",
    "error_code": -59,
    "error_msg": "integer overflow"
}
```
