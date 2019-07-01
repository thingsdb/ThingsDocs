## set_quota

> This code sets a quota on the number of things and disables the properties quota on collection *stuff*:

```python
import asyncio
from thingsdb.client import Client, scope

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        [
            set_quota('stuff', 'things', 10000),
            set_quota('stuff', 'properties', nil),
        ];
    ''', target=scope.thingsdb)
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -q << EOQ "
[
    set_quota('stuff', 'things', 10000),
    set_quota('stuff', 'properties', nil),
];
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    null
]
```
Quota limits can be set on collections. The following quota limits can be set:

Type | Description
---- | -----------
`things` | Maximum number of [things](#thing) allowed in a collection.
`properties` | Maximum number of [properties](#properties) which can be assigned to a thing.
`array_size` | Maximum array length. This quota type applies to all [array type](#array-type).
`raw_size` | Maximum [raw](#string-raw) value size. When this quota is set, both queries and blob values are limited to this quota.

If a quota limit is reached, then the affected query will raise `MAX_QUOTA_ERROR`.

The current quota values can be viewed with [collection(...)](#collection) or [collections()](#collections).

This function generates an [event](#events).

### Function
`set_quota(collection, quota_type, quota)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
collection | raw/int (required) | Collection *name* or *id*.
quota_type | raw (required) | Must be one of `'things'`, `'properties'`, `'array_size'` or `'raw_size'`.
quota | int/nil (required) | Integer value to set the quota limit or `nil` to disable the quota.

### Return value
`nil` when successful.