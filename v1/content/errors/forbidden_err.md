---
title: "forbidden_err"
weight: 356
---

Returns an [error](../../data-types/error) when the client or user is missing the required privileges.

This function does *not* generate a [change](../../overview/changes).

### Function

`forbidden_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***forbidden_err()***:

```thingsdb,json_response
forbidden_err();
```

> Return value in JSON format

```json
"forbidden (access denied)"
```
