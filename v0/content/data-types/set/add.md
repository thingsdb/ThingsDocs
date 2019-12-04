---
title: "add"
weight: 47
---

Adds new thing to the [set](..) and returns the number of things which are
actually added to the set. For example `my_set.add(#42);` will return `0`
if `my_set` already contains thing `#42`.

This function generates an [event](../../../overview/events).

### Function

*set*.`add(thing1, thing1, ..., thingX)`

### Return value

Returns the number of `things` which are added to the set.

### Example

> This code adds things to a set:

```thingsdb,json_response
s = set();
a = {item: 'a'};
b = {item: 'b'};

// add both `a` and `b` to set `s`; note that `a` is only added once;
s.add(a, a, b);
```

> Return value in JSON format

```json
2
```
