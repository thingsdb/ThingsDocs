---
title: "revoke"
weight: 279
---

Revoke, collection or general, privileges from a user. See [grant](../../thingsdb-api/grant) for more information on
how access privileges can be set for a user.

To use this function, at least `CHANGE` privileges on the `@thingsdb` scope and `GRANT` privileges on the target scope are required.

This function generates a [change](../../overview/changes).

### Function

`revoke(target, user, mask)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`target` | int/raw | Can be either the `@node`, `@thingsdb`, or a `@collection` [scope](../../overview/scopes).
`user` | str | User to revoke privileges from.
`mask` | int | Bit-mask for revoking privileges.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the user or target
does not exist.

### Example

> Revoke all privileges for user `iris` on collection `stuff`:

```thingsdb,syntax_only,@t
revoke('@:stuff', 'iris', FULL);
```

> Return value in JSON format

```json
null
```
