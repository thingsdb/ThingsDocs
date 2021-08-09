---
title: "restart_module"
weight: 250
---

Restarts a given module on the select node scope.

{{% notice tip %}}
If you want to restart the module on *all* nodes, you can use the [deploy_module(*name*, *nil*)](../../thingsdb-api/deploy_module) function with `nil` as second argument.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`restart_module(name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | Module to restart.

### Return value

Returns `nil`.

### Example

> This code will reset the counters on a node:

```thingsdb,syntax_only,@n
restart_module('DEMO');
```

> Return value in JSON format

```json
null
```
