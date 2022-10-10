---
title: "set_password"
weight: 333
---

Change a user's password. This function can also be used to remove an existing
password by using `nil` as the new password.

Passwords must contain 1 to 128 printable characters.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope when a `username`
other then the logged in user is given as argument. For the currently logged in user, `CHANGE`
privileges on the `@thingsdb` scope are sufficient.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`set_password(username, new_password)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
username | str (required) | Name of the user
new_password | nil/str (required) | New password or `nil`

### Return value

Returns `nil` if successful. A [lookup_err()](../../errors/lookup_err) is returned
if the user does not exist and [bad_data_err()](../../errors/bad_data_err) if the new password is not compliant.

### Example

> This code changes the password for user *admin*:

```thingsdb,syntax_only,@t
// Change the password for user `admin`
set_password('admin', 'my_secret_password');
```

> Return value in JSON format

```json
null
```
