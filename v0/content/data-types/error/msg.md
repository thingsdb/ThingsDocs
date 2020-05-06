---
title: "msg"
weight: 38
---

Returns the error *message* of an [error](..) type.

This function does *not* generate an [event](../../../overview/events).

### Function

*error*.`msg()`

### Arguments

None

### Return value

Returns error message of an error.

### Example

> This code uses `code()` to return the error code for an error:

```thingsdb,json_response
type_err("incorrect type").msg();
```

> Return value in JSON format

```json
"incorrect type"
```
