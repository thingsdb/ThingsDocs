---
title: "get"
weight: 118
---

Return the value of a property on a [thing](..) by a given property name.
If the property is not found then the return value will be `nil`, unless an alternative
return value is given.

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`get(name [, alt])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | Name of the property where to return the value for.
alt | any (optional) | Optional return value.

### Return value

Returns the value for the given property name. If the property is not found the the
return value will be `nil`  unless an alternative return value is given as second argument.

### Example

> This code shows an example use case of ***get()***:

```thingsdb,json_response
tmp = {name: 'Iris'};
tmp.get('name');
```

> Return value in JSON format

```json
"Iris"
```
