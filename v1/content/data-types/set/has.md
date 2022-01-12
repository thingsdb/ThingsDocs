---
title: "has"
weight: 109
---

Determines if a [set](..) has a given thing.

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`has(thing)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
thing | thing (required) | Thing to check.

### Return value

Returns `true` if the given thing is found in the set and otherwise `false`.

### Example

> This code shows an example use case of ***has()***:

```thingsdb,json_response
iris = {name: 'Iris'};
s = set(iris);

/* Check if iris is in set `s` */
s.has(iris);
```

> Return value in JSON format

```json
true
```
