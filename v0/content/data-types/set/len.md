---
title: "len"
weight: 98
---

Returns the length of a [set](..).

This function does *not* generate an [event](../../../overview/events).

### Function

*set*.`len()`

### Arguments

None

### Return value

Returns length of the set.

### Example

> This code uses `len()` to return the number of items in a set:

```thingsdb,json_response
set({item: 'a'}, {item: 'b'}).len();
```

> Return value in JSON format

```json
2
```
