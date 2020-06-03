---
title: "grant"
weight: 199
---

Grant, collection or general, privileges to a user. Access to a user is provided by setting
a bit mask to either the `@node`, `@thingsdb` or a `@collection`  [scope](../../overview/scopes).

To use this function, at least `MODIFY` privileges on the `@thingsdb` scope and `GRANT` privileges on the target scope are required.

{{% notice warning %}}
It is not possible to set privileges on a specific node scope. Therefore scope `@node` will apply to *all* nodes in ThingsDB.
{{% /notice %}}

The following pre-defined masks are available:

Mask         | Description
------------ | -----------
`READ` (1)   | Gives read access.
`MODIFY` (2) | Gives read and modify access.
`GRANT` (4)  | Gives read, modify and grant (and revoke) privileges.
`WATCH` (8)  | Gives watch (and un-watch) privileges.
`RUN` (16)   | Gives run procedures access.
`FULL` (31)  | A *mask* for full privileges.

{{% notice note %}}
It is not possible to have `GRANT` privileges without also having `MODIFY` privileges.
Similarly, it is not possible to have `MODIFY` privileges without `READ`. However, ThingsDB
automatically applies the required privileges so when setting for example `GRANT` privileges, ThingsDB
makes sure that the user also gets `MODIFY` and `READ`.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`grant(target, user, mask);`

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

> Grant read and watch privileges to user `iris` to collection `stuff`:

```thingsdb,json_response,@t
new_user('iris');
new_token('iris');

// Assign WATCH privileges on all node scopes to user `iris`
grant('@node', 'iris', WATCH);

// Assign READ and WATCH privileges on collection `stuff` to user `iris`
grant('@:stuff', 'iris', READ|WATCH);
```

> Return value in JSON format

```json
null
```