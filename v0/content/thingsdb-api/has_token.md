---
title: "has_token"
weight: 222
---

Determines if a token exists in ThingsDB.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`has_token(key)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
key | str (required) | Token key to check.

### Return value

Returns `true` if the token exists and otherwise `false`.

### Example

> This code shows an example use case of ***has_token()***:

```thingsdb,json_response,@t
has_token('XXXXXXXXXXXXXXXXXXXXXX');
```

> Return value in JSON format

```json
false
```
