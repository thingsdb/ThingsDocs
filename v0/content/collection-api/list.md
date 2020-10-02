---
title: "list"
weight: 159
---

Returns a new empty [list](../../data-types/list) or returns a list for a given `set`.

This function does *not* generate an [event](../../overview/events).

### Function

`list([value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | set/list/tuple (optional) | Optional value to initialize the list.

### Return value

A new list.

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
