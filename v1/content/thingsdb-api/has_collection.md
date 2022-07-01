---
title: "has_collection"
weight: 304
---

Determines if a collection exists in ThingsDB.

This function does *not* generate a [change](../../overview/changes).

### Function

`has_collection(collection)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
collection | str/int (required) | Collection name or Id to check.

### Return value

Returns `true` if the collection exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_collection()***:

```thingsdb,json_response,@t
has_collection('stuff');
```

> Return value in JSON format

```json
true
```
