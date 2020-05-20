---
title: "has_enum"
weight: 122
---

Determines if a [enumerator type](../../data-types/enum) exists in the current `@collection` scope.

This function does *not* generate an [event](../../overview/events).

### Function

`has_enum(enum)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str (required) | [Enum](../../data-types/enum) name to check.

### Return value

Returns `true` if a [enumerator type](../../data-types/enum) with a given name exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_enum()***:

```thingsdb,json_response
has_enum('XXX');
```

> Return value in JSON format

```json
false
```
