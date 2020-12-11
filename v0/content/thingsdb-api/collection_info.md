---
title: "collection_info"
weight: 227
---

Returns information about a specific collection.

This function requires `READ` privileges on the requested `collection`, or `MODIFY`
privileges on the `@thingsdb` scope.

This function does *not* generate an [event](../../overview/events).

### Function

`collection_info(collection)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
collection | str/int (required) | Name or Id of the collection

### Return value

Returns [info](../../data-types/info) about the collection.

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
    "name": "stuff",
    "things": 61352,
    "time_zone": "UTC"
}
```
