---
title: "array"
weight: 123
---

Returns a new empty [list](../../data-types/list) or returns a list for a given `set`.

This function does *not* generate an [event](../../events).

### Function

`array([set])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
set | set (optional) | Optional set to initialize the array.

### Return value

A new array.

> This code shows some return values for ***array()***:

```thingsdb,json_response
array( set({}, {}) );
```

> Return value in JSON format

```json
[
    {},
    {}
]
```
