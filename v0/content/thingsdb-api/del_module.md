---
title: "del_module"
weight: 239
---

Delete a module. A `SIGTERM` signal will be send to the process for the module which might cancel running futures.

This function generates an [event](../../overview/events).

### Function

`del_module(name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | Name of the module to delete.

### Return value

Returns `nil` when successful.

### Example

> This code will delete module *DEMO*:

```thingsdb,syntax_only,@t
// Delete module `DEMO`
del_module('DEMO');
```
