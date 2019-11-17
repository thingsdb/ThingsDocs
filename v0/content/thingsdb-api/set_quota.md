---
title: "set_quota"
weight: 18
---

Quota limits can be set on collections. The following quota limits can be set:

Type | Description
---- | -----------
`things` | Maximum number of [things](../../data-types/thing) allowed in a collection. [Type](../../data-types/type) instances are also counted towards this quota.
`properties` | Maximum number of [properties](../../properties) which can be assigned to a thing.
`array_size` | Maximum [list](../../data-types/list) and [tuple](../../data-types/tuple) length.
`raw_size` | Maximum [str](../../data-types/str) and [bytes](../../data-types/bytes) length.

If a quota limit is reached, then the affected query will raise `MAX_QUOTA_ERROR`.

The current quota values can be viewed with [collection(...)](../../thingsdb-api/collection_info) or [collections()](../../thingsdb-api/collections_info).

This function generates an [event](../../events).

### Function
`set_quota(collection, quota_type, quota)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
collection | str/int (required) | Collection *name* or *id*.
quota_type | str (required) | Must be one of `'things'`, `'properties'`, `'array_size'` or `'raw_size'`.
quota | int/nil (required) | Integer value to set the quota limit or `nil` to disable the quota.

### Return value
`nil` when successful.

> This code sets a quota on the number of things and disables the properties quota on collection *stuff*:

```thingsdb,json_response,@t
[
    set_quota('stuff', 'things', 10000),
    set_quota('stuff', 'properties', nil),
];
```

> Return value in JSON format

```json
[
    null,
    null
]
```