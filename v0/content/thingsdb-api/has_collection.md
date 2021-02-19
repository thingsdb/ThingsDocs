---
title: "has_collection"
weight: 250
---

Determines if a collection exists in ThingsDB.

This function does *not* generate an [event](../../overview/events).

### Function

`has_collection(collection)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
collection | str/int (required) | Collection name or id to check.

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
