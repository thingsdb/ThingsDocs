---
title: "set_module_scope"
weight: 362
---

Modules can be restricted for usage in a single scope. This can be a `@collection:..` scope, but also a `@node` or `@thingsdb` scope.
This function can be used to change the module scope. When the scope is set to `nil`, the module can be used in any scope.

This function generates a [change](../../overview/changes).

### Function

`set_module_scope(name, scope)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
name | str (required) | Name of the module.
scope | str/nil (required) |

### Return value

Returns `nil` if successful.

### Example

> This code changes the module configuration for module *DEMO*:

```thingsdb,syntax_only,@t
// Restrict module usage to collection `stuff`
set_module_scope('DEMO', '//stuff');
```

> Return value in JSON format

```json
null
```
