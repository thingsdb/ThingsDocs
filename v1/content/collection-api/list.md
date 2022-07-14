---
title: "list"
weight: 235
---

Returns a new empty [list](../../data-types/list) or returns a list for a given `set`.

This function does *not* generate a [change](../../overview/changes).

### Function

`list([value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | set/list/tuple (optional) | Optional value to initialize the list. If the argument is already a *list* or *tuple*, the return value will be the same *list* or *tuple*.

### Return value

A new list *(Unless the given argument was a tuple or list, then no conversion takes place and the given list or tuple will be the return value)*.

### Example

> This code shows some return values for ***list()***:

```thingsdb,json_response
list( set({}, {}) );
```

> Return value in JSON format

```json
[
    {},
    {}
]
```
