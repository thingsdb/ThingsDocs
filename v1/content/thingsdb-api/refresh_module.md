---
title: "refresh_module"
weight: 361
---

Refresh module first stops the module (if running), next if will check for an update and performs the update if required. When finished, it will start the module again.

This function generates a [change](../../overview/changes).

### Function

`refresh_module(name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`name` | str (required) | Name of the module to refresh.

### Return value

Returns `nil`. You might want to use [module_info(..)](../module_info) to check if the module is successfully running. If not, the node logging might give you additional information about the cause of the error.

### Example

> Refresh module `demo`:

```thingsdb,syntax_only,@t
refresh_module('demo');
```

> Return value in JSON format

```json
null
```
