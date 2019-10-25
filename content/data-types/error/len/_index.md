---
title: "len"
date: 2019-10-23T16:41:37+02:00
---

Returns the length of an [error](..) message.

This function does *not* generate an [event](../../../events).

### Function

*error*.`len()`

### Arguments

None

### Return value

Returns length of an error message.

> This code uses `len()` to return the length of the error message:

```thingsdb,json_response
err().len();
```

> Return value in JSON format

```json
10
```
