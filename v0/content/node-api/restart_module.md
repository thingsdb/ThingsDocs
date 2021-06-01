---
title: "restart_module"
weight: 246
---

Restarts a given module.

This function does *not* generate an [event](../../overview/events).

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
