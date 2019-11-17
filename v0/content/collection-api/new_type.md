---
title: "new_type"
weight: 144
---

Creates a new [Type](../../data-types/type). This function *only* creates a new type
and does not allow you to specify any fields. With the [set_type()](../set_type) function
you can define the fields for the new type.

{{% notice note %}}
It is possible to use `set_type` directly without calling `new_type` first. However, sometimes
you want to cross reference two types so you want both type to exists before calling `set_type`.
{{% /notice %}}


This function generates an [event](../../events).

### Function

`new_type(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | string | Name of the Type to be created.

### Return value

The name of the newly created Type.

> This code shows the return value for ***new_type()***:

```thingsdb,json_response
new_type('MyType');
```

> Return value in JSON format

```json
"MyType"
```
