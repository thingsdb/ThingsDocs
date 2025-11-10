---
title: "whitelist_add"
weight: 385
---

A whitelist can be configured for both rooms and procedures. This whitelist determines which specific rooms and procedures a user is allowed to access.

**Procedures:**
- **No Whitelist:** All procedures are allowed by default, given that the user has at least `RUN` privileges for the scope and (`RUN|CHANGE` for procedures making changes).
- **Empty Whitelist:** All procedures are blocked.
- **Whitelist with Rules:** Only procedures matching a rule in the whitelist are allowed (the user also need `RUN` privileges for the scope or `RUN|CHANGE` for procedures making changes).

**Rooms:**
- **No Whitelist:** All rooms are allowed by default, given that the user has `JOIN` privileges for the scope.
- **Empty Whitelist:** All rooms are blocked.
- **Whitelist with Rules:** Only rooms with a name applied (see [set_name](../../data-types/room/set_name)), and matching a rule in the whitelist are allowed (the user also need `JOIN` privileges for the scope).

Whitelists are applied globally, regardless of the scope.

Use regular expressions to create flexible rules that match multiple rooms or procedures at once.

By carefully defining whitelist rules, you can precisely control a user's access to specific rooms and procedures within your system.

Specific rules or the entire whitelist can be removed using the see [whitelist_del](../whitelist_del) function.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`whitelist_add(user, whitelist, [rule])`

### Arguments

Argument    | Type                  | Description
----------- | --------------------- | -----------
`user`      | str (required)        | Username for which to add the whitelist.
`whitelist` | str (required)        | The whitelist. Either `"procedures"` or `"rooms"`.
`rule`      | str/regex (optional)  | Either a name for a specific procedure/room or a regular expression to match potentially multiple procedures or rooms. If omitted, an empty whitelist will be created.

### Return value

Returns `nil` if successful.

### Example

> Create a new user `iris` and apply a whitelist.

```thingsdb,json_response,@t
new_user('iris');
grant('//stuff', 'iris', RUN|CHANGE|JOIN);

whitelist_add('iris', 'rooms', /^api_.*/);
whitelist_add('iris', 'procedures', /^api_.*/);

user_info('iris').load().whitelists;
```

> Return value in JSON format

```json
{
    "procedures": [
        "/^api_.*/"
    ],
    "rooms": [
        "/^api_.*/"
    ]
}
```

With this configuration, 'iris' can access rooms and procedures in the '//stuff' collection whose names begin with 'api_'. Access to other procedures and rooms is restricted.
