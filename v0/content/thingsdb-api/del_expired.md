---
title: "del_expired"
weight: 23
---

Delete all expired tokens.

This function generates an [event](../../events).

### Function
`del_expired();`

### Arguments
None

### Return value
Returns `nil`.

> This code will delete all expired tokens:

``````thingsdb,should_pass,@t
// Delete all expired tokens
del_expired();
```
