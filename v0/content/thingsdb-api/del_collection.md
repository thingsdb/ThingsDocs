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
name | str (required) | Name of the collection to delete.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the collection does not exist.

> This code will delete collection *stuff*:

```thingsdb,should_pass,@t
// Delete collection `stuff`
del_collection('stuff');
```