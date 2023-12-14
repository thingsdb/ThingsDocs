---
title: "len"
weight: 37
---

Returns the length of the bytes value.

This function does *not* generate a [change](../../../overview/changes).

### Function

*bytes*.`len()`

### Arguments

None

### Return value

Returns length of the byte sequence.

### Example

> This code uses `len()` to return the length of a byte sequence:

```thingsdb,json_response
bytes("abc").len();
```

> Return value in JSON format

```json
3
```
