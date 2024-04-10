---
title: "set_time_zone"
weight: 368
---


The default time zone for the *@node* and *@thingsdb* scopes has been set to *UTC* and collections will inherit the time zone from the *@thingsdb* scope so they also have *UTC* as their default as long as the *@thingsdb* scope is not changed.
This function can be used to change the time zone for a scope.

{{% notice warning %}}
**Be careful** with changing the time zone as this changes the behavior for functions like [datetime(..)](../../collection-api/datetime) and [timeval(..)](../../collection-api/timeval).
{{% /notice %}}

See [time_zones_info()](../../collection-api/time_zones_info) for a list of all available timezones.

Use `datetime().zone();` to view the current time zone in a scope.

This function generates a [change](../../overview/changes).

### Function

`set_time_zone(scope, zone)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
scope | str (required) | Specify the [scope](../../overview/scopes) to change the time zone for.
zone | str (required) | New time zone.

### Return value

Returns `nil` if successful.

### Example

> This code changes the password for user *admin*:

```thingsdb,json_response,@t
// Change the time zone to Europe/Amsterdam
set_time_zone('//stuff', 'Europe/Amsterdam');
```

> Return value in JSON format

```json
null
```
