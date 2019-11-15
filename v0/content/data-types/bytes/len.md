---
title: "len"
date: 2019-10-23T13:54:12+02:00
---

Returns the length of the bytes value.

This function does *not* generate an [event](../../../events).

### Function
*bytes*.`len()`

### Arguments
None

### Return value
Returns length of the byte sequence.

> This code uses `len()` to return the length of a byte sequence:

```thingsdb,json_response
bytes("abc").len();
```

> Return value in JSON format

```json
3
```
