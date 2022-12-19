---
title: "zero_div_err"
weight: 374
---

Returns an [error](../../data-types/error) when an attempt is made to divide or take a modulo by zero.

This function does *not* generate a [change](../../overview/changes).

### Function

`zero_div_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***zero_div_err()***:

```thingsdb,json_response
zero_div_err();
```

> Return value in JSON format

```json
"division or module by zero"
```
