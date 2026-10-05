---
title: "clear"
weight: 60
---

Removes all items from a [dict](..).

This function generates a [change](../../../overview/changes)

### Function

*dict*.`clear()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> This code adds things to a set:

```thingsdb,json_response
d = dict(range(10).map(|i| [uuid(), i]));

assert( d.len() == 10 );  // dict with 10 items

d.clear();
assert( d.len() == 0 );  // the dict is empty

d;
```

> Return value in JSON format

```json
[]
```
