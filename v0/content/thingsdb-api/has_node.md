---
title: "has_node"
weight: 252
---

Determines if a node exists in ThingsDB.

This function does *not* generate an [event](../../overview/events).

### Function

`has_node(id)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
id | int (required) | Node Id to check.

### Return value

Returns `true` if a node with a given Id exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_node()***:

```thingsdb,json_response,@t
has_node(0);
```

> Return value in JSON format

```json
true
```
