---
title: "syntax_err"
weight: 221
---

Returns an [error](../../data-types/error) when the given ThingsDB code contains a syntax error.

This function does *not* generate an [event](../../overview/events).

### Function

`syntax_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value.

### Example

> This code shows ***syntax_err()***:

```thingsdb,json_response
syntax_err();
```

> Return value in JSON format

```json
{
    "!": "syntax_err()",
    "error_code": -52,
    "error_msg": "syntax error in query"
}
```
