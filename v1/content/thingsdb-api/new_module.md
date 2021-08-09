---
title: "new_module"
weight: 274
---

Create (and configure) a new module for ThingsDB.

After a module is created, a [future()](../../data-types/future/#modules) is required to use the new module.

ThingsDB has special support for Python modules which will be activated if you module file ends with `.py`. In this case the [Python interpreter](../../getting-started/configuration) will be used to start the module.

{{% notice tip %}}
By default a **module** can be used in all scopes. It is possible however, to restrict the usage by using [set_module_scope(..)](../set_module_scope).
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`new_module(name, file, [configuration])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`name` | str (required) | Name of the new module.
`file` | str (required) | Filename of the module. The same file might be configured multiple times. The file must be path relative to the [modules path](../../getting-started/configuration)). If the file ends with `.py`, the Python interpreter will be used to start the module.
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
