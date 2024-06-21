---
title: "ren"
weight: 176
---

Rename a property on a [thing](..).

{{% notice info %}}
While almost all functions on *things* are also available on *Type instances*, this one is not. This is because a Type instance has a fixed set of properties and so you are not allowed to rename one of them on a single instance.
Use [mod_type()](../../../collection-api/mod_type/ren) instead, to rename the property on *all* instances if this is what you want.
{{% /notice %}}

This function generates a [change](../../../overview/changes).

### Function

*thing*.`ren(old, new)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
old      | str (required) | Name of the property to rename.
new      | str (required) | New name of the property.

### Return value

Returns `nil`.

### Example

> This code shows some return values for ***ren()***:

```thingsdb,json_response
.x = 42;
.ren('x', 'y');  // rename .x to .y
```

> Return value in JSON format

```json
null
```
