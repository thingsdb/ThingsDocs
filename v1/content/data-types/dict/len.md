---
title: "len"
weight: 68
---

Returns the number of items in a [dict](..).

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`len()`

### Arguments

None

### Return value

Returns the number of items in a dict.

### Example

> This code uses `len()` to return the number of items in a dict:

```thingsdb,json_response
dict([
    [0, 'item 0'],
    [1, 'item 1'],
]).len();
```

> Return value in JSON format

```json
2
```
