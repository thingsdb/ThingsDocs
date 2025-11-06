---
title: "is_module"
weight: 247
---

This function determines whether the provided value is a [module](../../../modules) value or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_module(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a module, else it returns `false`.

### Example

> This code shows some return values for ***is_module()***:

```thingsdb,json_response
is_module(123);
```

> Return value in JSON format

```json
false
```
