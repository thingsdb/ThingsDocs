---
title: "del_expired"
weight: 152
---

Delete all expired tokens.

This function generates an [event](../../overview/events).

### Function

`del_expired();`

### Arguments

None

### Return value

Returns `nil`.

### Example

> This code will delete all expired tokens:

```thingsdb,should_pass,@t
// Delete all expired tokens
del_expired();
```
