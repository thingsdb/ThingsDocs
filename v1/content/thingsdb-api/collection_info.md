---
title: "collection_info"
weight: 337
---

Returns information about a specific collection.

This function requires `QUERY` privileges on the requested `collection`, or `CHANGE`
privileges on the `@thingsdb` scope.

This function does *not* generate a [change](../../overview/changes).

### Function

`collection_info(collection)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
collection | str/int (required) | Name or Id of the collection

### Return value

Returns [mpdata](../../data-types/mpdata) about the collection.

### Example

> Returns information about collection *stuff*:

```thingsdb,should_pass,@t
collection_info('stuff');
```

> Example return value in JSON format

```json
{
    "collection_id": 782,
    "created_at": 1579175900,
    "default_deep": 1,
    "name": "stuff",
    "next_free_id": 93114,
    "things": 61352,
    "time_zone": "UTC"
}
```
