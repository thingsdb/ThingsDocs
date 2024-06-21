---
title: "fill"
weight: 77
---

Fills a list with a given value.

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*list*.`fill(item)`

### Return value

Returns the filled _list_.

### Example

> This code creates a list with five nil values

```thingsdb,json_response
range(5).fill(nil);
```

> Return value in JSON format

```json
[null, null, null, null, null]
```
