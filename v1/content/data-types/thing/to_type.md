---
title: "to_type"
weight: 169
---

Converts a *[thing](../../thing)* into a *[typed](../../typed)* thing.

Before a thing may be converted, *all* the properties of the thing must have an exact match with the properties defined by the Type.
It you later want to change tome properties, the function [mod_type](../../../collection-api/mod_type) can be used.

Since the root of a collection is also a *thing*, it is possible to use this function to make the collection strict.

{{% notice note %}}
It is not possible to convert a thing into a Type with [relations](../../../collection-api/mod_type/rel). Relations *can* be made *after* the conversion.
{{% /notice %}}

{{% notice warning %}}
Although it is possible to convert a *typed* thing to a *non-typed* thing using the [to_thing](../../typed/to_thing) function, this ***only works*** if the type is not dependent of any other type (including self dependencies). This is because ThingsDB is not able to tell if it is allowed to convert back to a *non-typed* thing when it might be required by a parent of the *typed* thing.
{{% /notice %}}

This function generates a [change](../../../overview/changes).

### Function

*thing*.`to_type(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the [Type](../../../overview/type) to convert the thing into.

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
