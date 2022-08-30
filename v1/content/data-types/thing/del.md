---
title: "del"
weight: 153
---

Delete a property from a [thing](..).

{{% notice info %}}
While almost all functions on *things* are also available on *Type instances*, this one is not. This is because a Type instance has a fixed set of properties and so you are not allowed to delete one of them on a single instance.
Use [mod_type()](../../../collection-api/mod_type/del) instead, to delete the property from *all* instances if this is what you want.
{{% /notice %}}

This function generates a [change](../../../overview/changes).

### Function

*thing*.`del(property)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
property | str (required) | Name of the property to delete.

### Return value

Returns the removed value if successful. A [lookup_err()](../../../errors/lookup_err) is returned
if the property does not exist or [bad_data_err()](../../../errors/bad_data_err) in case the given property is
not a valid [name](../../../overview/names).

{{% notice warning %}}
In versions before **v0.9.3** the return value of `.del(..)` used to be `nil` when successful.
{{% /notice %}}

### Example

> This code shows some return values for ***del()***:

```thingsdb,json_response
.x = 'create and delete this prop';
.del('x');
```

> Return value in JSON format

```json
"create and delete this prop"
```
