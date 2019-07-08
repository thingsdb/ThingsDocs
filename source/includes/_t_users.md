## users

Returns user information for all users withing ThingsDB.

See the [user()](#user) function documentation for an example of the exposed user information.

This function requires `GRANT` privileges on the `:thingsdb` scope since it
exposes user access and token information.

This function does *not* generate an [event](#events).

### Function
`users()`

### Arguments
None

### Return value
Returns an array containing user information for all users within ThingsDB.