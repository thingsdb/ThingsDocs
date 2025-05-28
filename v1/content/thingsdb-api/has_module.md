---
title: "has_module"
weight: 354
---

Determines if a module exists in ThingsDB. The scope restriction of the module has no impact on the result of this function.

This function does *not* generate a [change](../../overview/changes).

### Function

`has_module(name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | Module to check.

### Return value

Returns `true` if the module exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_module()***:

```thingsdb,json_response,@t
has_module('DEMO5');
```

> Return value in JSON format

```json
false
```
