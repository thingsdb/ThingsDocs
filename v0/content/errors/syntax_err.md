---
title: "syntax_err"
weight: 177
---

Returns an [error](../../data-types/error).

This function does *not* generate an [event](../../events).

### Function
`syntax_err([message])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value
An error value.

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
