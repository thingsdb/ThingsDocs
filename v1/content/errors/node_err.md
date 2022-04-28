---
title: "node_err"
weight: 354
---

Returns an [error](../../data-types/error) when a node was not able to handle the request.

This function does *not* generate a [change](../../overview/changes).

### Function

`node_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***node_err()***:

```thingsdb,json_response
node_err();
```

> Return value in JSON format

```json
"node is temporary unable to handle the request"
```
