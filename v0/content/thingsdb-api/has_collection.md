---
title: "has_collection"
weight: 167
---

Determines if a collection exists in ThingsDB.

This function does *not* generate an [event](../../overview/events).

### Function

`has_collection(name_or_id)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name_or_id | str/int (required) | Collection name or id to check.

### Return value

Returns `true` the collection exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_collection()***:

```thingsdb,json_response,@t
has_collection('stuff');
```

> Return value in JSON format

```json
true
```
