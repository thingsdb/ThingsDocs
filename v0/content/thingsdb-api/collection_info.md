---
title: "collection_info"
weight: 93
---

Returns information about a specific collection.

This function does *not* generate an [event](../../events).

### Function

`collection_info(name_or_id);`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
name_or_id | str/int | Name or Id of the collection

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
    "name": "stuff",
    "quota_array_size": null,
    "quota_properties": null,
    "quota_raw_size": null,
    "quota_things": null,
    "things": 61352
}
```