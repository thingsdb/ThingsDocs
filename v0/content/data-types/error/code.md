---
title: "code"
weight: 40
---

Returns the error *code* of an [error](..) type.

This function does *not* generate an [event](../../../overview/events).

### Function

*error*.`code()`

### Arguments

None

### Return value

Returns error code of an error.

### Example

> This code uses `code()` to return the error code for an error:

```thingsdb,json_response
type_err("incorrect type").code();
```

> Return value in JSON format

```json
-61
```
