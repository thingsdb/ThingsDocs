---
title: "Procedures API"
weight: 294
chapter: true
---

# Procedures API

A procedure in ThingsDB is a named closure that is attached to a scope and available to use in an API call.

Procedures can be used in the `@thingsdb` scope and in `@collection` scopes.

The same procedure name can be used in different scopes but must be unique within a scope.

### Related functions

Function | description
-------- | ----- | -----------
[del_procedure](./del_procedure) | Delete an existing procedure.
[has_procedure](./has_procedure) | Check if a procedure exists.
[new_procedure](./new_procedure) | Create a new procedure.
[procedure_doc](./procedure_doc) | Get the docstring of a procedure.
[procedure_info](./procedure_info) | Show information about a procedure.
[procedures_info](./procedures_info) | Show information about all procedures in the current scope.
[rename_procedure](./rename_procedure) | Rename an existing procedure.
[run](./run) | Run a procedure.

### Examples

Below is an example where we make a procedure in the `@thingsdb` scope to help us create a user in ThingsDB with some
pre-defined access rights and a token for one day usage.

```thingsdb,should_pass,@t
new_procedure('create_user', |name| {
    "Creates a new user with a token and some basic access rights.";

    // Create the user
    new_user(name);

    // Create a `token` for one day
    token = new_token(name, datetime().move('days', 1));

    // Give join, query and run privileges on collection `stuff`
    grant('@:stuff', name, JOIN|QUERY|RUN);

    // Return the token
    token;
});
```

Once a procedure is created, it can be easily used in a query. You may just call the procedure as if it is a function, or you can use the [run](./run) function in one of the native ThingsDB clients available (see the example below) or by performing a `RUN` request using the HTTP API (see [connect](../connect/http-api/#run-request) section). For a more low-level example view the [socket run example](../connect/socket/run).

> Here is a complete working example where we use the Python client to call our procedure.

```python
import asyncio
from thingsdb.client import Client

client = Client()
loop = asyncio.get_event_loop()

async def create_user(name):
    # first we need to connect, in this example we assume ThingsDB is running
    # on localhost and the default admin user can be used
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')

    # this is the code where we call our procedure
    token = await client.run('create_user', name, scope='@thingsdb')

# run the example
loop.run_until_complete(create_user('iris'))

# the will close the client in a nice way
client.close()
loop.run_until_complete(client.wait_closed())
```

It is also possible to use the procedure within a query or from another procedure. This can be done with the [run](./run) function.

> Here is an example where we use the `create_user` procedure in a query.

```thingsdb,should_pass,@t
// Our procedure requires a change so we need to use `wse`
token = wse(create_user('cato'));

// return the token
token;
```

> Example output in JSON format

```json
"Sj3WQ3dkm8Hl8B/iFoH9Cz"
```

{{% notice note %}}
Prior to version **v0.10.13** it was not possible to call a procedure just by it's name. Instead the `run(..)` function was required. Thus, the above example would need to be written as: `token = wse(run('create_user', 'cato'));`.
{{% /notice %}}

