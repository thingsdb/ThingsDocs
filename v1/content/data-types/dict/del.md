---
title: "del"
weight: 62
---

Delete a item from a [dict](..) by its key.

This function generates a [change](../../../overview/changes).

### Function

*dict*.`del(key)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
key | str/int/uuid (required) | Key for the item to delete.

### Return value

Returns the removed value if successful. A [lookup_err()](../../../errors/lookup_err) is returned if the key does not exist.

### Example

> This code shows some return values for ***del()***:

```thingsdb,json_response
d = dict([[123, 'Hello ThingsDB!']]);
d.del(123);
```

> Return value in JSON format

```json
"Hello ThingsDB!"
```
