---
title: "deep"
date: 2019-10-14T09:57:18+02:00
weight: 7
---

Returns the current `deep` value. The `deep` value might change when a function with a [return(..)](../../collection-api/return) is called which has changed the `deep` value for this query.

This function does *not* generate an [event](../../events).

### Function
`deep()`

### Arguments
None

### Return value
The current `deep` value for the running query.

> This code uses `deep()` to return the default `deep` value:

```thingsdb,json_response
deep();  // returns the default since `deep` is not changed
```

> Return value in JSON format

```json
1
```
