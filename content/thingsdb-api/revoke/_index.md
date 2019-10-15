---
title: "revoke"
date: 2019-10-14T09:51:20+02:00
weight: 16
---

Revoke collection or general privileges from a user. See [grant](../../thingsdb-api/grant) for more information on
how access privileges can be set for a user.

This function generates an [event](../../events).

### Function
`revoke(target, user, mask);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`target` | int/raw | Can be either the `.node` scope, `.thingsdb` scope, or a collection name or id.
`user` | raw | User to revoke privileges from.
`mask` | int | Bit-mask for revoking privileges.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the user or target
does not exist.

> Revoke all privileges for user `iris` on collection `stuff`:

```
revoke('stuff', 'iris', FULL);
```

> Return value in JSON format

```json
null
```
