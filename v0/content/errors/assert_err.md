---
title: "assert_err"
weight: 168
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`assert_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

### Example

> This code shows ***assert_err()***:

```thingsdb,json_response
assert_err();
```

> Return value in JSON format

```json
{
    "!": "assert_err()",
    "error_code": -50,
    "error_msg": "assertion statement has failed"
}
```
