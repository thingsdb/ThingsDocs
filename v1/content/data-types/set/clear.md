---
title: "clear"
weight: 96
---

Removes all things from a [set](..).

This function generates a [change](../../../overview/changes) *(except when called on a [variable](../../../overview/variable))*.

### Function

*set*.`clear()`

### Return value

Returns `nil`.

### Example

> This code adds things to a set:

```thingsdb,json_response
a = {item: 'a'};
b = {item: 'b'};
s = set(a, b);

s.clear();
s;  // the set is empty
```

> Return value in JSON format

```json
[]
```
