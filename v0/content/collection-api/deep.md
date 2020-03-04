---
title: "deep"
weight: 104
---

Returns the current `deep` value for the running query. The deep value indicates how far down the result of a query is returned. For example, *thing1* may contain a *thing2* that contains a *thing3*. A deep value of 1 would only show the content of *thing1* and a deep value of 3 will go as deep as the content of *thing3*. 

The `deep` value changes when a function with a [return(..)](../../collection-api/return) is called which has changed the `deep` value for this query.

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
