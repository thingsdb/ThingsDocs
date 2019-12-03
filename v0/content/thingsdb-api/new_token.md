---
title: "new_token"
weight: 155
---

Adds a new token for a given user. An optional expiration time may be given after which the token cannot
be used anymore. Use [del_expired](../../thingsdb-api/del_expired) to cleanup expired tokens. The expiration time may be
given as a UNIX time-stamp in seconds or a date/time string.

Some valid date/time strings:

- `2021-01-01`
- `2023-02-06 14:30`
- `2023-07-5T13:23:20+01:00`

Expiration dates in the past are not allowed an will raise a [bad_data_err()](../../errors/bad_data_err) error.

It is also possible to set a description for the token which can be used to identify where token is used for.
If you only want to set a description, but no expiration time, then you can use `nil` as second argument.
For example: `new_token('my_user', nil, 'some nice description');`

There can be no more than 128 tokens assigned to a single user. A `MAX_QUOTA_ERROR` is raised if this limit
is reached. Existing tokens can be removed with [del_token](../../thingsdb-api/del_token) and to view the current tokens you can use the [user_info(..)](../../thingsdb-api/user_info) (or [users_info()](../../thingsdb-api/users_info)) function.

This function generates an [event](../../overview/events).

### Function

`new_token(username, [, expiration_time] [, description]);`

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
// ThingsDB must be started on node2 using the `--secret ...` argument
new_token('admin', now() + 7*24*3600, 'token for one week');
```

> Example return value in JSON format (the token key)

```json
"8Ay0ngISFa9je3o/MMu24U"
```
