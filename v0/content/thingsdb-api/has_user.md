---
title: "has_user"
weight: 221
---

Determines if a user exists in ThingsDB.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`has_user(username)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
username | str (required) | User to check.

### Return value

Returns if `true` the user exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_user()***:

```thingsdb,json_response,@t
has_user('admin');
```

> Return value in JSON format

```json
true
```
