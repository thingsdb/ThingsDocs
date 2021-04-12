---
title: "user_info"
weight: 278
---

Returns information about a user. If no argument is given, this function will return
information about the currently logged in user.

{{% notice note %}}
This function requires `GRANT` privileges on the `@thingsdb` scope when a `username`
other then the logged in user is given as argument. For the currently logged in user, `QUERY`
privileges on the `@thingsdb` scope are sufficient.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`user_info([username])`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
username | str (optional) | Name of the user

### Return value

Returns [mpdata](../../data-types/mpdata) about the user.

### Example

> This code returns info for the authenticated user:

```thingsdb,should_pass,@t
// Without a `username`, info about the currently logged in user is returned
user_info();
```

> Example output in JSON format:

```json
{
    "access": [
        {
            "privileges": "FULL",
            "scope": "@node"
        },
        {
            "privileges": "FULL",
            "scope": "@thingsdb"
        },
        {
            "privileges": "FULL",
            "scope": "@collection:stuff"
        }
    ],
    "created_at": 1573981254,
    "has_password": true,
    "name": "admin",
    "tokens": [
        {
            "created_on": "2019-11-17T09:25:36Z",
            "expiration_time": "2020-11-17T09:25:36Z",
            "key": "QpVmHOsfQaKKpjpOkW0SUt",
            "status": "OK"
        }
    ],
    "user_id": 1
}
```
