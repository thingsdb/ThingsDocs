---
title: "Procedures API"
weight: 265
chapter: true
---

# Procedures API

A procedure in ThingsDB is a named closure that is attached to a scope and available to use in an API call.

Procedures can be used in the `@thingsdb` scope and in `@collection` scopes.

The same procedure name can be used in different scopes but must be unique within a scope.

Below is an example where we make a procedure in the `@thingsdb` scope to help us create a user in ThingsDB with some
pre-defined access rights and a token for one day usage.

```thingsdb,should_pass,@t
new_procedure('create_user', |name| {
    "Creates a new user with a token and some basic access rights.";

    // Create the user
    new_user(name);

    // Create a `token` for one day
    token = new_token(name, datetime().move('days', 1));

    // Give watch access to the @node scope and read on collection `stuff`
    grant('@node', name, WATCH);
    grant('@:stuff', name, QUERY|RUN);

    // Return the token
    token;
});
```

Once a procedure is created, it can be easily used via a [run](./run) function in one of the native ThingsDB clients available (see the example below) or by performing a `RUN` request using the HTTP API (see [connect](../connect/http-api/#run-request) section). For a more low-level example view the [socket run example](../connect/socket/run).

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

> Here is an example query where we use `run` to create a new user.

```thingsdb,should_pass,@t
// Our procedure has side-effects so we need to wrap `run` with `wse`
token = wse(run('create_user', 'cato'));

// return the token
token;
```

> Example output in JSON format

```json
"Sj3WQ3dkm8Hl8B/iFoH9Cz"
```
