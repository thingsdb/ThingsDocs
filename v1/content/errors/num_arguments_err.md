---
title: "num_arguments_err"
weight: 367
---

Returns an [error](../../data-types/error) when a wrong number of arguments is given.

This function does *not* generate a [change](../../overview/changes).

### Function

`num_arguments_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***num_arguments_err()***:

```thingsdb,json_response
num_arguments_err();
```

> Return value in JSON format

```json
"wrong number of arguments"
```
