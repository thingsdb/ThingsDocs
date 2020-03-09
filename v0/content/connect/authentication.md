---
title: "Authentication"
weight: 7
---

ThingsDB supports authentication by using a *user* and *password* combination, or with a *token*. A default user `admin` with password `pass` is created on a fresh installation.
If you did not yet change the default password, you might want to jump to [set password](../../thingsdb-api/set_password) or jump to [token authentication](#token-authentication).

It might be a good idea to create a [new user](../../thingsdb-api/new_user) with minimal privileges and add a [new token](../../thingsdb-api/new_token) for this user.
See the [grant](../../thingsdb-api/grant) and [revoke](../../thingsdb-api/revoke) functions for managing privileges for a user.

{{% notice note %}}
For connecting to ThingsDB with a auto-reconnect client, `WATCH` privileges on the `.node` scope are required.
{{% /notice %}}

## Token authentication

This is a small tutorial to create a *token* and remove the *password* for the default `admin` user.
This can be done with any client but in this tutorial the [HTTP API](../http-api) is used with simple `curl`
commands.

First we create a new token, and then we remove the password from the `admin` user.
Although this could be done in one step, we do this in *two* steps to be sure the new token
works before removing the password.

> Replace `127.0.0.1:9210` with the address and port where your node is listening on for API requests

```bash
curl --location --request POST 'http://127.0.0.1:9210/thingsdb' \
--header 'Content-Type: application/json' \
--user admin:pass \
--data-raw '{
    "type": "query",
    "code": "new_token('\''admin'\'');"
}'
```

The will return a JSON string containing a new token, for example: `"YyZcvq7BY3w+VgOTvXzTZp"`

We can now use this token key to remove the password from user `admin`:

```bash
curl --location --request POST 'http://127.0.0.1:9210/thingsdb' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YyZcvq7BY3w+VgOTvXzTZp' \
--data-raw '{
    "type": "query",
    "code": "set_password('\''admin'\'', nil);"
}'
```
