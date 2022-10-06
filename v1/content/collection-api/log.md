---
title: "log"
weight: 241
---

Might be used for debugging code. The message will be logged as a warning message on the console of the node which is processing the request.
When you are connected using a socket stream, then a [warning message](../../listening/warning) with code `2` will be send to the client as well.

This function does *not* generate a [change](../../overview/changes).

### Function

`log(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | str/any (required) | Value to log. If not a string, an attempt will be made to convert the value into a string. A [type_err()](../../errors/type_err) will be raised when the conversion has failed.

### Return value

Returns `nil`.

### Example

> Returns the reference count of a given value:

```thingsdb,json_response
log("Test.., one, two, three");
```

> Example return value in JSON format

```json
null
```
