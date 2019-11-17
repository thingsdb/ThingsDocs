---
title: "indexof"
weight: 70
---

Returns the first index at which a given value can be found in the [list](..) or [tuple](../../tuple), or `nil` if it is not present.
The index of an array starts at `0`, so the first item has index `0` the second `1` and so on.

This function does *not* generate an [event](../../../events).

### Function

*array*.`indexof(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any | The value to find the index for.

### Return value

Index at which the first item matches a given value, or `nil` if it is not present.

> This code shows an example using ***indexof()***:

```thingsdb,json_response
["January", "February", "March", "April"].indexof("March");
```

> Return value in JSON format

```json
2
```
