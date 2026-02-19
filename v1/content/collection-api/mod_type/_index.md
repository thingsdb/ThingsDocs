---
title: "mod_type"
weight: 291
---

This function is used to modify an existing [Type](../../overview/type). A number of actions can be performed with this function.

This function generates a [change](../../overview/changes) and requires a call to [commit()](../commit) if [commit history](../../thingsdb-api/set_history) is enabled for the scope.

### Actions

Action | Description
------ | -----------
[add](./add) | Adds a new property or method to the type.
[all](./all) | Iterates over all instances of a given type.
[del](./del) | Deletes a property or method from the type.
[hid](./hid) | Enable or disable *hide-id* for the type.
[idx](./idx) | Enable or disable *auto-index* for the type.
[mod](./mod) | Modifies a property or method definition.
[rel](./rel) | Creates a relation between types.
[ren](./ren) | Renames a property or method.
[wpo](./wpo) | Enable or disable *wrap-only* mode for the type.
