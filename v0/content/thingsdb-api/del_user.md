---
title: "del_user"
weight: 98
---

Delete a user. It is not possible to delete your own user account and a `BAD_REQUEST` will be raised in case you try to.
Any *tokens* associated with the user will also be deleted.

This function generates an [event](../../events).

### Function
`del_user(username);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
username | str (required) | Username of the user to delete.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the user does not exist.

> This code will delete user *test*:

```thingsdb,syntax_only,@t
// Delete user `test`
del_user('test');
```
