---
title: "del_token"
weight: 160
---

Delete a token.

This function generates an [event](../../overview/events).

### Function

`del_token(key);`

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
