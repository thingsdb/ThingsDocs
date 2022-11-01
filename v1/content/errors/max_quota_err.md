---
title: "max_quota_err"
weight: 364
---

Returns an [error](../../data-types/error) when a quota limit is reached.

This function does *not* generate a [change](../../overview/changes).

### Function

`max_quota_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***max_quota_err()***:

```thingsdb,json_response
max_quota_err();
```

> Return value in JSON format

```json
"max quota is reached"
```
