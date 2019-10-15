---
title: "has (set)"
date: 2019-10-14T09:59:47+02:00
weight: 17
---

Determines if a [set](../../data-types/set-type) has a given thing.

This function does *not* generate an [event](../../events).

### Function
*set*.`has(thing)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
thing | thing (required) | Thing to check.

### Return value
Returns `true` the given thing is found in the set and otherwise `false`.

> This code shows an example use case of ***has()***:

```
iris = {name: 'Iris'};
set = set(iris);

/* Check if iris is in the set */
set.has(iris);
```

> Return value in JSON format

```json
true
```
