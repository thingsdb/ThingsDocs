---
title: "root"
weight: 313
---

Returns the `root` for the current collection or `nil` when the current scope is not a collection scope.

This function does *not* generate a [change](../../overview/changes).

### Function

`root()`

### Arguments

None

### Return value

Returns the collection root.

### Example

> This code shows an example usage of ***root()***:

```thingsdb,should_pass
// calling .id() will run on the collection root so these are equal
.id() == root().id();
```

> Example return value in JSON format

```json
true
```
