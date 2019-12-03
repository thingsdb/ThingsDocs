---
title: "deep"
weight: 87
---

Returns the current `deep` value. The `deep` value might change when a function with a [return(..)](../../collection-api/return) is called which has changed the `deep` value for this query.

This function does *not* generate an [event](../../overview/events).

### Function

`deep()`

### Arguments

None

### Return value

The current `deep` value for the running query.

### Example

> This code uses `deep()` to return the default `deep` value:

```thingsdb,json_response
deep();  // returns the default since `deep` is not changed
```

> Return value in JSON format

```json
1
```
