---
title: "watch"
weight: 82
---

Subscribe for watching mutations on a stored [thing](..). If this function is called on a [thing](..) which is *not* stored, and therefore has no *#ID*, then a [value_err()](../../../errors/value_err) is raised.
This method returns `nil` but *always* triggers an [init event](../../../watching/on-init), even when an earlier call to this function has been made.

{{% notice warning %}}
This function *only* works with **socket** connections. When using this function with
an **HTTP API** request, it has no effect.
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`watch()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> This code shows how to use `watch()`:

```thingsdb,json_response
.watch();
```

> Return value in JSON format:

```json
null
```