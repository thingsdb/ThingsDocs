---
title: "unwatch"
weight: 96
---

Stop watching for mutations on a [thing](..).
This function returns `nil` and triggers a [stop event](../../../watching/on-stop), *only* when the thing was being watched.

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`unwatch()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> This code shows how to use `unwatch()`:

```thingsdb,json_response
.unwatch();
```

> Return value in JSON format:

```json
null
```
