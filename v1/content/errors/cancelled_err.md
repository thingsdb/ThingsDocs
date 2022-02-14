---
title: "cancelled_err"
weight: 358
---

Returns an [error](../../data-types/error) when an operation is cancelled before completion. Fox example by a time-out or stop of service.

This function does *not* generate a [change](../../overview/changes).

### Function

`cancelled_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***cancelled_err()***:

```thingsdb,json_response
cancelled_err();
```

> Return value in JSON format

```json
 "operation is cancelled before completion"
```
