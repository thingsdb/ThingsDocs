---
title: "set_password"
weight: 108
---

Change a users password. This function can also be used to remove an existing
password by using `nil` as the new password.

Passwords must contain 1 to 128 printable characters.

This function generates an [event](../../events).

### Function

`set_password(username, new_password);`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
username | str (required) | Name of the user
new_password | nil/str (required) | New password or `nil`

### Return value

Returns `nil` if successful. An `INDEX_ERROR` is returned
if the user does not exist and `BAD_REQUEST` if the new password is not compliant.

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
