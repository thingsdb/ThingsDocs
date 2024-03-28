---
title: "new_token"
weight: 354
---

Adds a new token for a given user. An optional expiration time may be given; after this time the token cannot
be used anymore. Use [del_expired](../../thingsdb-api/del_expired) to cleanup expired tokens. The expiration time may be
given as a [datetime](../../data-types/datetime) or [timeval](../../data-types/timeval) type.

Expiration dates in the past are not allowed an will raise a [bad_data_err()](../../errors/bad_data_err) error.

It is also possible to set a description for the token which can be used to identify the token.
If you only want to set a description, but no expiration time, then you can use `nil` as a second argument.
For example: `new_token('my_user', nil, 'some nice description');`

There can be no more than 128 tokens assigned to a single user. A [max_quota_err()](../../errors/max_quota_err) is raised if this limit
is reached. Existing tokens can be removed with [del_token](../../thingsdb-api/del_token) and to view the current tokens you can use the [user_info(..)](../../thingsdb-api/user_info) (or [users_info()](../../thingsdb-api/users_info)) function.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope when a `username`
other then the logged in user is given as argument. For the currently logged in user, `CHANGE`
privileges on the `@thingsdb` scope are sufficient.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`new_token(username, [, expiration_time] [, description])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
username | str (required) | Name of the user.
expiration_time | nil/int/float/raw (optional) | Expiration date of the token.
description | str (optional) | Token description.

### Return value

Returns the new token key.

### Example

> Create a new token for user `admin`:

```thingsdb,should_pass,@t
// A new token with an expiration date in one week and description
new_token('admin', datetime().move('weeks', 1), 'token for one week');
```

> Example return value in JSON format (the token key)

```json
"8Ay0ngISFa9je3o/MMu24U"
```
