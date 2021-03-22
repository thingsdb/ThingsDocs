---
title: "new_user"
weight: 264
---

Creates a new user to ThingsDB. The new user is created without a password, token and access privileges.
You probably want to [set a password](../../thingsdb-api/set_password) or add a [new token](../../thingsdb-api/new_token), and assign some privileges using [grant(...)](../../thingsdb-api/grant).

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`new_user(user)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`user` | str (required) | Username, between 1 and 128 *graphical* characters.

### Return value

Returns the new user `id` if successful. A [lookup_err()](../../errors/lookup_err) is raised
if the user already exists.

### Example

> Create a new user `iris`:

```thingsdb,should_pass,@t
new_user('iris');
```

> Example return value in JSON format (the new user id)

```json
19
```
