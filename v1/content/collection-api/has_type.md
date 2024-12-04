---
title: "has_type"
weight: 224
---

Determines if a [Type](../../overview/type) exists in the current `@collection` scope.

This function does *not* generate a [change](../../overview/changes).

### Function

`has_type(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str (required) | [Type](../../overview/type) name to check.

### Return value

Returns `true` if a [Type](../../overview/type) with a given name exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_type()***:

```thingsdb,json_response
has_type('XXX');
```

> Return value in JSON format

```json
false
```
