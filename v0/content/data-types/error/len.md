---
title: "len"
weight: 26
---

Returns the length of an [error](..) message.

This function does *not* generate an [event](../../../overview/events).

### Function

*error*.`len()`

### Arguments

None

### Return value

Returns length of an error message.

### Example

> This code uses `len()` to return the length of the error message:

```thingsdb,json_response
type_err("incorrect type given").len();
```

> Return value in JSON format

```json
20
```
