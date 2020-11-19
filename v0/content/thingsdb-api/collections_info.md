---
title: "collections_info"
weight: 213
---

Returns collection information about all collections in ThingsDB.

See the [collection_info()](../../thingsdb-api/collection_info) function documentation for an example of the exposed collection information.

{{% notice note %}}
If the user has no **MODIFY** permissions on the `@thingsdb` scope, then only the collections where
the user has at least **READ** privileges are included in the result.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`collections_info()`

### Arguments

None

### Return value

List with collection [info](../../data-types/info)  about all collections in ThingsDB.
