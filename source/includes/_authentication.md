# Authentication

> To authorize, use this code:

```python
import asyncio
from thingsdb.client import Client

client = Client()
loop = asyncio.get_event_loop()


async def example():
    # replace `node.local` with your ThingsDB server address
    await client.connect('node.local')

    # replace `amdin` with yout username and `pass` with your password
    await client.authenticate(auth=['admin', 'pass'])

    # ..or by using a token
    await client.authenticate('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# run the example
loop.run_until_complete(example())

# the will close the client in a nice way
client.close()
loop.run_until_complete(client.wait_closed())
```

```shell
# Authenticate with a user and password
thingscmd -n node.local -u admin -p pass -q "nil;"
# ..or with a token
thingscmd -n node.local -t "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" -q "nil;"

```


ThingsDB supports authentication by using a *user* and *password* combination, or with a *token*. A default user `admin` with password `pass` is created on a fresh installation.
If you did not yet change the default password, you might want to jump to [set password](#set_password)

It might be a good idea to create a [new user](#new_user) with minimal privileges and add a [new token](#new_token) for this user.
See the [grant](#grant) and [revoke](#revoke) functions for managing privileges for a user.

<aside class="notice">
For connecting to ThingsDB with a auto-reconnect client, <code>WATCH</code> privileges on the <code>:node</code> scope are required.
</aside>


## Python

> Use pip to install the python client:

```
pip install python-thingsdb
```

The Python client supports both queries, watching and a framework for using ThingsDB in a really simple way.



## Shell

> Copy/paste to download and install *thingscmd*

```
pip install thingscmd
```

For running thingsdb queries from the shell, a shell tool [thingscmd](https://github.com/thingsdb/ThingsCMD) is available.
It is not possible to *watch* things by using this shell based tool.
