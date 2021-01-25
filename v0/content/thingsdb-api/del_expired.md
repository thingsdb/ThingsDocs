---
title: "del_expired"
weight: 237
---

Delete all expired tokens.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`del_expired()`

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
