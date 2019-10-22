---
title: "set_password"
date: 2019-10-14T09:51:37+02:00
weight: 17
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
username | raw (required) | Name of the user
new_password | nil/raw (required) | New password or `nil`

### Return value
Returns `nil` if successful. An `INDEX_ERROR` is returned
if the user does not exist and `BAD_REQUEST` if the new password is not compliant.

> This code changes the password for use *admin*:

```thingsdb,syntax_only,@t
// Change the password for user `admin`
set_password('admin', 'my_secret_password');
```

> Return value in JSON format

```json
null
```
