---
title: "value_err"
weight: 371
---

Returns an [error](../../data-types/error) when a given value has the correct type but contains invalid data.

This function does *not* generate a [change](../../overview/changes).

### Function

`value_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***value_err()***:

```thingsdb,json_response
value_err();
```

> Return value in JSON format

```json
"object has the right type but an inappropriate value"
```
