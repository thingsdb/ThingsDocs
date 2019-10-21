---
title: "has (thing)"
date: 2019-10-14T09:59:52+02:00
weight: 18
---

Determines if a [thing](../../data-types/thing-type) has a given property.

This function does *not* generate an [event](../../events).

### Function
*thing*.`has(name)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
name | raw (required) | Name of the property to check.

### Return value
Returns `true` when the given propery name is found and otherwise `false`.

> This code shows an example use case of ***has()***:

```thingsdb,json_response
tmp = {name: 'Iris'};
tmp.has('name');
```

> Return value in JSON format

```json
true
```
