---
title: "set_time_zone"
weight: 283
---


By default each collection will be created with time zone `UTC`. This function
can be used to change the time zone for a collection. If changed, the functions
[datetime(..)](../../collection-api/datetime) and [timeval(..)](../../collection-api/timeval)
will use the collections time zone unless specified otherwise. See [time_zones_info()](../time_zones_info) for a list of all available timezones.

Use [collection_info(..)](../collection_info) to view the current time zone for a collection.

This function generates a [change](../../overview/changes).

### Function

`set_time_zone(collection, zone)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
collection | str/int (required) | Collection name or Id to change the time zone for.
zone | str (required) | New time zone.

### Return value

Returns `nil` if successful.

### Example

> This code changes the password for user *admin*:

```thingsdb,json_response,@t
// Change the time zone to Europe/Amsterdam
set_time_zone('stuff', 'Europe/Amsterdam');
```

> Return value in JSON format

```json
null
```
