---
title: "to_type"
weight: 132
---

Converts a *thing* into an instance of a given [Type](../../type).

Before a thing may be converted, *all* the properties of the thing must have an exact match with the properties defined by the Type.
It you later want to change tome properties, the function [mod_type](../../../collection-api/mod_type) can be used.

Since the root of a collection is also a *thing*, it is possible to use this function to make the collection strict.

{{% notice note %}}
It is not possible to convert a thing into a Type with [relations](../../../collection-api/mod_type/rel). Relations *can* be made *after* the conversion.
{{% /notice %}}

{{% notice warning %}}
This function works only on a thing and can not be undone. **Converting a thing is therefore permanent**.
{{% /notice %}}

This function generates an [event](../../../overview/events).

### Function

*thing*.`to_type(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the [Type](../../type) to convert the thing into.

### Return value

Returns `nil` when successful.

### Example

> This code converts a collection into a Type using the ***to_type()*** function:

```thingsdb,json_response
// Create a type `Root`
set_type('Root', {
    name: 'str'
});

// Create a name property so the collection will match with type `Root`
.name = 'Example';

// Convert the collection into type `Root`
.to_type('Root');
```

> Return value in JSON format

```json
null
```
