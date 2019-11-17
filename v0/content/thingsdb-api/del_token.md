---
title: "del_token"
weight: 97
---

Delete a token.

This function generates an [event](../../events).

### Function
`del_token(key);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
key | str (required) | Token key to delete.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the token is not found.

> This code will delete a token:

``````thingsdb,syntax_only,@t
// Delete a token
del_token('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
```
