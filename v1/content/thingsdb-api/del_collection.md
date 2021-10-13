---
title: "del_collection"
weight: 261
---

Delete a collection.

This function generates a [change](../../overview/changes).

### Function

`del_collection(name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | Name of the collection to delete.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the collection does not exist.

### Example

> This code will delete collection *stuff*:

```thingsdb,should_pass,@t
// Delete collection `stuff`
del_collection('stuff');
```
