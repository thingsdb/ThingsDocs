---
title: "del_token"
date: 2019-10-14T09:49:34+02:00
weight: 6
---

Delete a token.

This function generates an [event](../../events).

### Function
`del_token(key);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
key | raw (required) | Token key to delete.

### Return value
Returns `nil` when successful. An `INDEX_ERROR` is raised if the token is not found.

> This code will delete a token:

``````thingsdb,syntax_only,@t
// Delete a token
del_token('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
```
