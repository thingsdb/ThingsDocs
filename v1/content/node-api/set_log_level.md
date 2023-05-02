---
title: "set_log_level"
weight: 308
---

Change the log level for the node in the selected scope.

ThingsDB will then log all levels greater than or equal to the specified level.
For example, a default log_level of **warning** will log **warning**, **error** and **critical** messages.

This function does *not* generate a [change](../../overview/changes).

### Log Levels

Name  | Int | Description
----- | --- | ----
DEBUG | 0 | Display debug messages (can result in large amount of logging).
INFO | 1 | Informational messages.
WARNING | 2 | Warning messages (default log level).
ERROR | 3 | Error messages, can occur if for example a node is not available.
CRITICAL | 4 | Critical messages, should never occur unless something is really wrong.

### Function

`set_log_level(log_level)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
log_level | int | Log level to set on the node.

### Return value

Returns `nil`.

### Example

> Change the log level on the node in the selected scope to `debug`:

```thingsdb,json_response,@n
// Enable `debug` logging on the node in the selected scope
set_log_level(DEBUG);
```

> Return value in JSON format

```json
null
```
