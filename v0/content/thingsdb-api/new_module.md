---
title: "new_module"
weight: 257
---

Configures a new module for ThingsDB.

{{% notice tip %}}
By default a **module** can be used in all scopes. It is possible however, to restrict the usage by using [set_module_scope(..)](../set_module_scope).
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`new_module(name, file, [configuration])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`name` | str (required) | Username, between 1 and 128 *graphical* characters.
`file` | str (required) | Filename of the module. The same file might be configured multiple times. The file must be path relative to the [modules path](../../getting-started/configuration))
`configuration` | any (optional) | Configuration for the module. The configuration will be packed using a fixed [deep](../../collection-api/deep) value of two (`2`). If omitted (or `nil`), no configuration will be used for the module.

### Return value

Returns `nil`. You might want to use [module_info(..)](../module_info) to check if the module is successfully running.

### Example

> Create a new module `DEMO1`:

```thingsdb,json_response,@t
new_module('DEMO1', 'demo');
```

> Return value in JSON format

```json
null
```
