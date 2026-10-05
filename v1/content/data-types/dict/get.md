---
title: "get"
weight: 65
---

Return the value of a item in a [dict](..) by a given key.
If the key is not found then the return value will be `nil`, unless an alternative
return value is given.

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`get(name, [alt])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | uuid/int/str (required) | The key where to return the value for.
alt | any (optional) | Optional return value.

### Return value

Returns the value for the given key. If the key is not found then the
return value will be `nil`, unless an alternative return value is given as second argument.

### Example

> This code shows an example use case of ***get()***:

```thingsdb,json_response
tmp = dict([["name", "Iris"]]);
tmp.get('name');
```

> Return value in JSON format

```json
"Iris"
```
