---
title: "auth_err"
weight: 358
---

Returns an [error](../../data-types/error) when authentication has failed.

This function does *not* generate a [change](../../overview/changes).

### Function

`auth_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***auth_err()***:

```thingsdb,json_response
auth_err();
```

> Return value in JSON format

```json
"authentication error"
```
