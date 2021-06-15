---
title: "del_token"
weight: 256
---

Delete a token.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope unless the given token belongs
to the logged on user. In the latter case, only `EVENT` privileges are required.
{{% /notice %}}

This function generates an [event](../../overview/events).

### Function

`del_token(key)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
key | str (required) | Token key to delete.

### Return value

Returns `nil` when successful. A [lookup_err()](../../errors/lookup_err) is raised if the token is not found.

### Example

> This code will delete a token:

```thingsdb,syntax_only,@t
// Delete a token
del_token('XXXXXXXXXXXXXXXXXXXXXX');
```
