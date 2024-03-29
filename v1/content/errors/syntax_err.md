---
title: "syntax_err"
weight: 402
---

Returns an [error](../../data-types/error) when the given ThingsDB code contains a syntax error.

This function does *not* generate a [change](../../overview/changes).

### Function

`syntax_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***syntax_err()***:

```thingsdb,json_response
syntax_err();
```

> Return value in JSON format

```json
"syntax error in query"
```
