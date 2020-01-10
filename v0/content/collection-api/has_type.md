---
title: "has_type"
weight: 99
---

Determines if a [Type](../../data-types/type) exists in the current `@collection` scope.

This function does *not* generate an [event](../../overview/events).

### Function

`has_type(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str (required) | [Type](../../data-types/type) name to check.

### Return value

Returns `true` a [Type](../../data-types/type) with a given name exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_type()***:

```thingsdb,json_response
has_type('XXXXXXXXXXXXXXXXXXXXXX');
```

> Return value in JSON format

```json
false
```
