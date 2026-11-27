---
title: "module_info"
weight: 394
---

Returns information about a specific module.

Value | Description
------- | -----------
`conf` | Configuration for the module. *(Only visible when the user has `CHANGE` privileges in the `@thingsdb` scope)*
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the module was created.
`file` | Module file name.
`name` | Name of the module.
`restarts` | Number of time the module is restarted. Manual restarts are excluded and will reset the counter to zero. *(Only visible in a `@node` scope)*
`version` | If available, the version string of the module.
`doc` | If available, documentation or a documentation link.
`schema` | Since ThingsDB v1.12.0, the module manifest schema version (`1` or `2`; defaults to `1`).
`scope` | The module can only be used in this scope. When the scope is `nil`, the module can be used in any scope.
`status` | Status of the scope. The status must be `running` before the module can be used.
`tasks` | The number of running tasks (futures) for this module on the current node. When going into *away* mode, open tasks might be cancelled. *(Only visible in a `@node` scope)*

This function does *not* generate a [change](../../overview/changes).

### Function

`module_info(name)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
name | str/int (required) | Name of the module

### Return value

Returns [mpdata](../../data-types/mpdata) about the module.

### Example

> Returns information about module *DEMO*:

```thingsdb,syntax_only
module_info('DEMO');
```

> Example return value in JSON format

```json
{
    "schema": 1,
    "conf": null,
    "created_at": 1579175900,
    "file": "/usr/lib/thingsdb/modules/demo",
    "name": "DEMO",
    "restarts": 0,
    "scope": null,
    "status": "running",
    "tasks": 0,
}
```
