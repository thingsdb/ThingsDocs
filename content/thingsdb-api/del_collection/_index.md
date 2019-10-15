---
title: "del_collection"
date: 2019-10-14T09:49:09+02:00
weight: 3
---

Delete a collection.

This function generates an [event](../../events).

### Function
`del_collection(name);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
name | raw (required) | Name of the collection to delete.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the collection does not exist.

> This code will delete collection *old_things*:

```
// Delete collection `old_things`
del_collection('old_things');
```