---
title: "set_owner"
weight: 148
---

Change the owner of a task. The new owner must have at least **CHANGE** permissions on scope where the task is created.

{{% notice tip %}}
Changing the owner is useful if you plan to remove an existing user as removing a user will also delete the tasks of the user.
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
