---
title: "id"
weight: 197
---

Returns the `id` of a _wrapped_ [thing](..) or `nil` if the thing is not stored.

This function does *not* generate a [change](../../../overview/changes).

### Function

*`<Type>`*.`id()`

### Arguments

None

### Return value

Returns `id` of a wrapped thing or `nil` when the thing is not stored.

### Example

> This code uses `id()` to return a collection id:

```thingsdb,json_response
set_type('Person', {name: 'str', namelen: |this| this.name.len()});
alice = Person{name: 'Alice'};
w = alice.wrap();
w.id();  // returns the Id (same as w.unwrap().id(), still nil as alice is not stored)
```

> Example return value in JSON format

```json
null
```
