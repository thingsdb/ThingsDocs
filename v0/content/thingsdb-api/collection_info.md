---
title: "collection_info"
date: 2019-10-14T09:48:47+02:00
weight: 1
---

Returns information about a specific collection.

This function does *not* generate an [event](../../events).

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