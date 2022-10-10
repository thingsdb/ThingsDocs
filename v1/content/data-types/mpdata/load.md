---
title: "load"
weight: 98
---

Load [mpdata](..) into ThingsDB.

This function does *not* generate a [change](../../../overview/changes).

### Function

*mpdata*.`load()`

### Arguments

None

### Return value

Returns a ThingsDB object.

### Example

> This code uses `load()`:

```thingsdb,json_response,@t
admin = user_info('admin').load();

// `admin` is now a ThingDB object.
admin.name;
```

> Return value in JSON format

```json
"admin"
```
