---
title: "Authentication"
weight: 1
chapter: true
---

# Authentication

ThingsDB supports authentication by using a *user* and *password* combination, or with a *token*. A default user `admin` with password `pass` is created on a fresh installation.
If you did not yet change the default password, you might want to jump to [set password](../thingsdb-api/set_password).

It might be a good idea to create a [new user](../thingsdb-api/new_user) with minimal privileges and add a [new token](../thingsdb-api/new_token) for this user.
See the [grant](../thingsdb-api/grant) and [revoke](../thingsdb-api/revoke) functions for managing privileges for a user.

{{% notice note %}}
For connecting to ThingsDB with a auto-reconnect client, `WATCH` privileges on the `.node` scope are required.
{{% /notice %}}
