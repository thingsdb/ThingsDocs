---
title: "users_info"
weight: 333
---

Returns user information about all users in ThingsDB.

See the [user_info()](../../thingsdb-api/user_info) function documentation for an example of the exposed user information.

This function requires `GRANT` privileges on the `@thingdb` scope since it
exposes user access and token information.

This function does *not* generate a [change](../../overview/changes).

### Function

`users_info()`

### Arguments

None

### Return value

List with user [mpdata](../../data-types/mpdata) about all users in ThingsDB.
