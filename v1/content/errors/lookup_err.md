---
title: "lookup_err"
weight: 377
---

Returns an [error](../../data-types/error) when a requested resource is not found or when an index is out-of-range.

This function does *not* generate a [change](../../overview/changes).

### Function

`lookup_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***lookup_err()***:

```thingsdb,json_response
lookup_err();
```

> Return value in JSON format

```json
"requested resource not found"
```
