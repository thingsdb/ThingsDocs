---
title: "set_module_conf"
weight: 342
---

Change the module configuration. This will (re-send) the module configuration to the module. If the module was not started, ThingsDB will also auto-load the module and send the configuration.
Any Value is accepted as config but value `nil` will *not* be considered as a configuration and thus will *not* be send to the module.

This function generates a [change](../../overview/changes).

### Function

`set_module_conf(name, configuration)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
name | str (required) | Name of the module.
configuration | any/nil (required) | New configuration for the module. The configuration will be packed using a fixed [deep](../../collection-api/deep) value of two (`3`). Value `nil` is an exception and can be used if the module does not require any configuration.

### Return value

Returns `nil` if successful.

### Example

> This code changes the module configuration for module *DEMO*:

```thingsdb,syntax_only,@t
set_module_conf('DEMO', {
    user: 'admin',
    password: 'pass'
});
```

> Return value in JSON format

```json
null
```
