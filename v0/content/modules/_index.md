---
title: "Modules"
weight: 301
chapter: true
---

# Modules

ThingsDB can be extended with modules.


### Related functions

Function | scope | description
-------- | ----- | -----------
[del_module](../thingsdb-api/del_module) | `@thingsdb` | Delete a module.
[has_module](../thingsdb-api/has_module) | `@thingsdb` | Check if a module exists.
[module_info](../thingsdb-api/module_info) | *all scopes* | Show information about a module.
[modules_info](../thingsdb-api/modules_info) | *all scopes* | Show information about all module.
[new_module](../thingsdb-api/new_module) | `@thingsdb` | Create a new module.
[rename_module](../thingsdb-api/new_module) | `@thingsdb` | Rename an existing module.
[restart_module](../node-api/restart_module) | `@node` | Restart a module on a single node.
[set_module_conf](../thingsdb-api/set_module_conf) | `@thingsdb` | Change the module configuration.
[set_module_scope](../thingsdb-api/set_module_scope) | `@thingsdb` | Change the module scope.


### Building modules

Modules can be created in any language. For some languages there exists a library which makes
building a module an easy task. Refer below to a list of libraries and examples:

Language | Library | Example
-------- | ------- | -------
[Go](https://golang.org)  | [go-timod](https://github.com/thingsdb/go-timod) | [Demo](https://github.com/thingsdb/ThingsDB/tree/master/modules/go/demo) (echo-reply example)
[Python](https://www.python.org)  | [py-timod](https://github.com/thingsdb/py-timod) | [Demo](https://github.com/thingsdb/ThingsDB/tree/master/modules/python/demo.py) (echo-reply example)
