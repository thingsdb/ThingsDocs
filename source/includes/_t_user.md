## user

Without arguments, this function returns info about the connected user and in this case `READ` privileges on the `:thingsdb` scope are sufficient.
If used with a user argument, then this function requires `GRANT` privileges on the `:thingsdb` scope since it exposes user access and token information.

This function does *not* generate an [event](#events).