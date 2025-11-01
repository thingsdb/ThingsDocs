---
title: "grant"
weight: 353
---

Grant, collection or general, privileges to a user. Access to a user is provided by setting
a bit mask to either the `@node`, `@thingsdb` or a `@collection`  [scope](../../overview/scopes).

To use this function, at least `CHANGE` privileges on the `@thingsdb` scope and `GRANT` privileges on the target scope are required.

{{% notice warning %}}
It is not possible to set privileges on a specific node scope. Therefore scope `@node` will apply to *all* nodes in ThingsDB.
{{% /notice %}}

#### Whitelists

Whitelists provide fine-grained control over user access. Granting a user `CHANGE|JOIN|RUN` permissions in conjunction with a whitelist enables the creation of user accounts that can only execute specified procedures and join designated rooms. See the [whitelist_add](../whitelist_add) and [whitelist_del](../whitelist_del) functions.

#### Permissions

The following predefined masks are available:

Mask         | Description
------------ | -----------
`QUERY` (1)  | Grants access to execute queries.
`CHANGE` (2) | Grants access to make changes.
`GRANT` (4)  | Grants administrative privileges, allowing users to grant and revoke permissions to other users.
`JOIN` (8)   | Grants join (and leave) privileges to a room.
`RUN` (16)   | Grants access to run procedures directly. Without `CHANGE`, only procedures without changes are allowed.
`USER` (27)  | A *mask* for `QUERY`, `CHANGE`, `JOIN` and `RUN`.
`FULL` (31)  | A *mask* for full privileges.

{{% notice note %}}
It is not possible to have `GRANT` privileges without also having `CHANGE` privileges.
However, ThingsDB automatically applies the required privileges so when setting for example `GRANT` privileges, ThingsDB
makes sure that the user also gets `CHANGE` privileges.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`grant(target, user, mask)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`target` | int/raw | Can be either the `@node`, `@thingsdb`, or a `@collection` [scope](../../overview/scopes).
`user` | str | User to grant privileges to.
`mask` | int | Bit-mask for setting privileges.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the user or target
does not exist.

### Example

> Grant query and join privileges to user `iris` to collection `stuff`:

```thingsdb,json_response,@t
new_user('iris');
new_token('iris');

// Assign QUERY and JOIN privileges on collection `stuff` to user `iris`
grant('@:stuff', 'iris', QUERY|JOIN);
```

> Return value in JSON format

```json
null
```
