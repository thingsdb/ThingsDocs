---
title: "operation_err"
weight: 363
---

Returns an [error](../../data-types/error) when an operation is not valid within the current context.

This function does *not* generate a [change](../../overview/changes).

### Function

`operation_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***operation_err()***:

```thingsdb,json_response
operation_err();
```

> Return value in JSON format

```json
"operation is not valid in the current context"
```
