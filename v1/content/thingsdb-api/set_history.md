---
title: "set_history"
weight: 379
---

Enables _"commit history"_ for a given scope. Commit history can be enabled for collections scopes and the @thingsdb scope.

{{% notice warning %}}
Disabling commit history will **permanently delete** all existing historical records for this scope. This action **cannot be undone**.
{{% /notice %}}

When enabled, the following functions require a [commit(..)](../../collection-api/commit) before they can be used:
- [new_type](../../collection-api/new_type)
- [set_type](../../collection-api/set_type)
- [mod_type](../../collection-api/mod_type)
- [del_type](../../collection-api/del_type)
- [to_type](../../data-types/thing/to_type) _(only required when used on the collection [root](../../collection-api/root))_
- [rename_type](../../collection-api/rename_type)
- [set_enum](../../collection-api/set_enum)
- [mod_enum](../../collection-api/set_enum)
- [del_enum](../../collection-api/set_enum)
- [rename_enum](../../collection-api/rename_enum)
- [new_procedure](../../procedures-api/new_procedure)
- [mod_procedure](../../procedures-api/mod_procedure)
- [del_procedure](../../procedures-api/del_procedure)
- [rename_procedure](../../procedures-api/rename_procedure)

Use the [history()](../../thingsdb-api/history) function to view the commits in the history log and [del_history()](../../thingsdb-api/del_history) to remove commits from the history log.

This function generates a [change](../../overview/changes).

### Function

`set_history(scope, state)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`scope`  | str  | Can be either the `@thingsdb` or a `@collection` [scope](../../overview/scopes).
`state`  | bool | `true` to enable commit history, `false` to disable commit history.

### Return value

The value `nil`.

### Example

> This code enables commit history for the "stuff" collection:

```thingsdb,syntax_only,@t
set_history('//stuff', true);
```

> Return value in JSON format

```json
null
```
