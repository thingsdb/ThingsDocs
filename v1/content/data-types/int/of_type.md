---
title: "of_type"
weight: 85
---

Returns the stored ThingsDB instance of a specific type matching the given ID.

{{% notice note %}}
The stored thing must already be of the specified type. For example, if `#3` is an instance of type `F`, `(3).of_type('T')` will fail. This function validates the type rather than converting it.
{{% /notice %}}

When the type name is known at write-time, the constructor syntax is preferred:

```thingsdb,should_pass
// Shorthand syntax for a static type
T(123);

// Equivalent using of_type
(123).of_type('T');
```

The `of_type()` method is primarily useful when the type name is determined dynamically from a variable or input.

To apply a type to a list of IDs at once, see [map_type()](../../list/map_type).

This function does *not* generate a [change](../../../overview/changes).

### Function

*int*.`of_type(Type)`

### Arguments

Argument | Arguments   | Description
-------- | ----------- | -----------
Type     | str         | The type name of the instance.

### Return value

Returns the instance of the specified type.

### Example

> Dynamically instantiate an object using a variable type name:

```thingsdb,json_response
// Given a dynamic type name variable
type_name = "T";

// Fetch instance #42 of type "T"
(42).of_type(type_name);
```

> Example return value in JSON format

```json
{
    "#": 42
}
```
