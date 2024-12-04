---
title: "Modules"
weight: 384
chapter: true
---

# Modules

ThingsDB can be extended with modules. A module is a binary file or Python code which accepts input from ThingsDB and returns with a response.
Each module will be started by ThingsDB as a separate process. For Python code this means that a Python interpreter is started for every module.
Modules keep running as long as ThingsDB is alive, but may be restarted from within ThingsDB using [restart_module()](../node-api/restart_module) on a single node, or with [deploy_module()](../thingsdb-api/deploy_module) and/or [refresh_module()](../thingsdb-api/refresh_module) which can be used to restart/re-install a module on *all* nodes.

See the [hello world module](./hello-world-module) section below for a tutorial on how to create and use modules in ThingsDB.

### Related functions

Function | scope | description
-------- | ----- | -----------
[del_module](../thingsdb-api/del_module) | `@thingsdb` | Delete a module.
[deploy_module](../thingsdb-api/deploy_module) | `@thingsdb` | Deploy code for a module.
[refresh_module](../thingsdb-api/refresh_module) | `@thingsdb` | Refresh a module. This will stop, update *(if required)*, and re-start a module.
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
[Go](https://golang.org)  | [go-timod](https://github.com/thingsdb/go-timod) | [Demo](https://github.com/thingsdb/module-go-demo) (echo-reply example)
[Python](https://www.python.org)  | [py-timod](https://github.com/thingsdb/py-timod) | [Demo](https://github.com/thingsdb/module-py-demo) (echo-reply example)

### Available modules

See the [supported modules](./supported-modules) section for a list of modules maintained by the ThingsDB team.

{{% notice tip %}}
We like to build a list of additional modules, contact <info@thingsdb.io> if you have a module you want to introduce to the world
{{% /notice %}}


