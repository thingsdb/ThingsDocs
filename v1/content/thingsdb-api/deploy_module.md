---
title: "deploy_module"
weight: 344
---

Deploy a module on all nodes. The module must be configured first, using the [new_module()](../new_module) function. This function is used to write the module data *(or plain python code)* to the module.
After deploying the code, the module will be restarted on every node.

{{% notice warning %}}
Before deploying a module, it is strongly recommended to use a **development** environment before deploying the module into production.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`deploy_module(name, data/new source)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`name` | str (required) | Name of the module to deploy the new code for.
`data` | str/bytes/nil (required) | **Only for modules with a file based source**. Data for the module. When `nil`, no data will be overwritten but the module *will* be restarted on all nodes. This might be useful if you want to force a module restart on all nodes. Type `str` is only allowed for Python modules.
`new source` | str | **Only for modules with a repository based source**. New source for the module. The module will stop, check for a new version using the new source, and next re-start the module.

### Return value

Returns `nil`. You might want to use [module_info(..)](../module_info) to check if the module is successfully running. If not, the node logging might give you additional information about the cause of the error.

### Example

> Create a new python module `ECHO` and deploy the code using `deploy_module(..)`:

```thingsdb,json_response,@t
// Create a new (python) module
new_module('ECHO', 'echo.py');

// Deploy the module code
deploy_module('ECHO',
"from timod import start_module, TiHandler, LookupError


class Handler(TiHandler):

    async def on_config(self, cfg):
        pass  # no config required

    async def on_request(self, req):
        if 'message' not in req:
            raise LookupError('missing `message` in request')

        return req['message']


if __name__ == '__main__':
    start_module('echo', Handler())

");
```

> Return value in JSON format

```json
null
```
