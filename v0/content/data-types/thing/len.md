---
title: "len"
weight: 129
---

Returns the number of items in a [thing](..).

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`len()`

### Arguments

None

### Return value

Returns the number of items in a thing.

### Example

> This code uses `len()` to return the number of items in a thing:

```thingsdb,json_response
{name: 'Iris', age: 6}.len();
```

> Return value in JSON format

```json
2
```
