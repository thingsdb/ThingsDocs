---
title: "has_timer"
weight: 295
---

Determines if a timer exists in the current scope.

This function does *not* generate an [event](../../overview/events).

### Function

`has_timer(timer)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
timer | int (required) | Timer Id to check.

### Return value

Returns `true` if a timer with a given Id exists in the current scope and otherwise `false`.

### Example

> This code shows an example use case of ***has_timer()***:

```thingsdb,json_response,@t
has_timer(123);
```

> Example return value in JSON format

```json
false
```
