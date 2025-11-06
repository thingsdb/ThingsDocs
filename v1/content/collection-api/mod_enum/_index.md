---
title: "mod_enum"
weight: 282
---

This function is used to modify an existing [enumerator type](../../data-types/enum). A number of actions can be performed with this function.

This function generates a [change](../../overview/changes) and requires a call to [commit()](../commit) if [commit history](../../thingsdb-api/set_history) is enabled for the scope.

### Actions

Action | Description
------ | -----------
[add](./add) | Adds a member or method to the enumerator.
[def](./def) | Sets the default member for the enumerator.
[del](./del) | Deletes a member or method from the enumerator.
[mod](./mod) | Modifies a members value or methods closure.
[ren](./ren) | Renames a member or method.
