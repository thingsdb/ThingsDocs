---
title: "json_load"
weight: 230
---

Converts a JSON [string](../../data-types/str) into a ThingsDB value.

This function does *not* generate a [change](../../overview/changes).

### Function

`json_load(string)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
string | str | JSON string to convert.

### Return value

ThingsDB value.

### Example

> This code shows an example for *json_load*:

```thingsdb,json_response
json_load('{"success": true}');
```

> Return value in JSON format

```json
{
    "success": true
}
```
