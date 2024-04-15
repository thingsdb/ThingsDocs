---
title: "type_err"
weight: 405
---

Returns an [error](../../data-types/error) when a given value is of the incorrect type.

This function does *not* generate a [change](../../overview/changes).

### Function

`type_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***type_err()***:

```thingsdb,json_response
type_err();
```

> Return value in JSON format

```json
"object of inappropriate type"
```
