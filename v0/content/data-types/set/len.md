---
title: "len"
weight: 1150
---

Returns the length of a [set](..).

This function does *not* generate an [event](../../../events).

### Function

*set*.`len()`

### Arguments

None

### Return value

Returns length of the set.

> This code uses `len()` to return the number of items in a set:

```thingsdb,json_response
set({iten: 'a'}, {item: 'b'}).len();
```

> Return value in JSON format

```json
2
```
