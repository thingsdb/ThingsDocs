---
title: "overflow_err"
weight: 405
---

Returns an [error](../../data-types/error) when an attempt is made to create an integer value out of the supported 64Bit (signed) range.

This function does *not* generate a [change](../../overview/changes).

### Function

`overflow_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***overflow_err()***:

```thingsdb,json_response
overflow_err();
```

> Return value in JSON format

```json
"integer overflow"
```
