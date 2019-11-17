---
title: "has"
weight: 60
---

Determines if a [thing](..) has a given property.

This function does *not* generate an [event](../../../events).

### Function

*thing*.`has(name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | Name of the property to check.

### Return value

Returns `true` when the given propery name is found and otherwise `false`.

> This code shows an example use case of ***has()***:

```thingsdb,json_response
tmp = {name: 'Iris'};

/* Check if `tmp` has a property `name` */
tmp.has('name');
```

> Return value in JSON format

```json
true
```
