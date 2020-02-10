---
title: "users_info"
weight: 179
---

Returns user information for all users in ThingsDB.

See the [user_info()](../../thingsdb-api/user_info) function documentation for an example of the exposed user information.

This function requires `GRANT` privileges on the `@thingdb` scope since it
exposes user access and token information.

This function does *not* generate an [event](../../overview/events).

### Function
`users_info()`

### Arguments
None

### Return value
List with user [info](../../data-types/info) for all users in ThingsDB.