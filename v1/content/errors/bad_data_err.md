---
title: "bad_data_err"
weight: 413
---

Returns an [error](../../data-types/error) when a request is malformed.

This function does *not* generate a [change](../../overview/changes).

### Function

`bad_data_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***bad_data_err()***:

```thingsdb,json_response
bad_data_err();
```

> Return value in JSON format

```json
"unable to handle request due to invalid data"
```
