---
title: "set_default_deep"
weight: 313
---

The *deep* value determines how many levels of data are returned by a query. Only *things* count towards this value. See [deep()](../../collection-api/deep) for more info about the *deep* value.

The default *deep* value for the *@node* and *@thingsdb* scopes has been set to `127`, this is the maximum value. Collections will inherit the *deep* value from the *@thingsdb* scope so they also have `127` as their default unless the *@thingsdb* scope is changed.

This function can be used to change the *deep* value for a scope.

{{% notice warning %}}
**Be careful** with changing the *deep* value as this will effect queries where *deep* has not explicitly been specified.
{{% /notice %}}

Use `deep();` to view the current *deep* value in a scope.

This function generates a [change](../../overview/changes).

### Function

`set_default_deep(scope, deep)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
scope | str (required) | Specify the [scope](../../overview/scopes) to change the time zone for.
deep | int (required) | New *deep* value, between `0` and `127`.

### Return value

Returns `nil` if successful.

### Example

> This code changes the password for user *admin*:

```thingsdb,json_response,@t
// Change the default deep value for collection "stuff" to 1
set_default_deep('//stuff', 1);
```

> Return value in JSON format

```json
null
```
