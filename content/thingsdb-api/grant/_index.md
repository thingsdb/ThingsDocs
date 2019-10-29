---
title: "grant"
date: 2019-10-14T09:49:48+02:00
weight: 8
---

Grant collection or general privileges to a user. Access to a user is provided by setting
a bit mask to either the `.node` scope, `.thingsdb` scope or a collection.
Privileges to ThingsDB gives a user the ability to view counters, add, view remove users etc.

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
Similarly, it is not possible to have `MODIFY` privileges without `READ`.
{{% /notice %}}

This function generates an [event](../../events).

### Function
`grant(target, user, mask);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`target` | int/raw | Can be either the `.node` scope, `.thingsdb` scope, or a collection name or id.
`user` | str | User to grant privileges to.
`mask` | int | Bit-mask for setting privileges.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the user or target
does not exist.

> Grant read and watch privileges to user `iris` to collection `stuff`:

```thingsdb,json_response,@t
new_user('iris');
new_token('iris');
[
    grant('@node', 'iris', WATCH),
    grant('@:stuff', 'iris', (READ|WATCH)),
];
```

> Return value in JSON format

```json
[
    null,
    null
]
```