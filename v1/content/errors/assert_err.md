---
title: "assert_err"
weight: 355
---

Returns an [error](../../data-types/error) when an assertion has failed.

This function does *not* generate a [change](../../overview/changes).

### Function

`assert_err([message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
message | str (optional) | Alternative error message.

### Return value

An error value *(in a client response, an error value will be packed as a string value with the error message)*.

### Example

> This code shows ***assert_err()***:

```thingsdb,json_response
assert_err();
```

> Return value in JSON format

```json
"assertion statement has failed"
```
