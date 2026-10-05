---
title: "has"
weight: 66
---

Determines if a given key exists in a [dict](..).

This function does *not* generate a [change](../../../overview/changes).

### Function

*dict*.`has(key)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
key | uuid/int/str (required) | Key to check.

### Return value

Returns `true` if the given key is found in the dict and otherwise `false`.

### Example

> This code shows an example use case of ***has()***:

```thingsdb,json_response
d = dict([[42, "The answer to everything"]]);

/* Check if the dict has a key 42 */
d.has(42);
```

> Return value in JSON format

```json
true
```
