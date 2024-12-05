---
title: "index_of"
weight: 85
---

The function returns the first index of the item in a [list](..) or [tuple](../../tuple) that matches the provided value, otherwise `nil` if it is not present.
The index of an array starts at `0`, so the first item has index `0` the second `1` and so on.

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`index_of(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any | The value to find the index for.

### Return value

Index at which the first item matches a given value, or `nil` if it is not present.

### Example

> This code shows an example using ***index_of()***:

```thingsdb,json_response
["January", "February", "March", "April"].index_of("March");
```

> Return value in JSON format

```json
2
```
