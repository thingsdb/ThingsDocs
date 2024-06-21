---
title: "set_owner"
weight: 159
---

Change the owner of a task. The new owner must have at least **CHANGE** permissions on scope where the task is created and access rights may not exceed the access rights of the user who is calling this method.

{{% notice tip %}}
Changing the owner is useful if you plan to remove an existing user _(removing a user will also delete the tasks of the user)_.
{{% /notice %}}

This function generates a [change](../../../overview/changes).

### Function

*task*.`set_owner(name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | Name of the new owner.

### Return value

Returns `nil` when successful.
