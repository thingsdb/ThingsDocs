---
title: "rename_user"
weight: 183
---

Rename a user.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function
`rename_user(current_name, new_name);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
`current_name` | str (required) | Current user name.
`new_name` | str (required) | New name for the user.

### Return value
Returns `nil` when successful.
