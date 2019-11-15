---
title: "del_expired"
date: 2019-10-14T09:49:19+02:00
weight: 4
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
