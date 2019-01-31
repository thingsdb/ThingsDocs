---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - python
  - shell

toc_footers:
  - Source on <a href='https://github.com/thingsdb/ThingsDocs'>GitHub</a>

includes:
  - types
  - root
  - functions
  - errors

search: true
---

# Introduction

Welcome to the ThingsDB API!

We have language bindings in Python! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.



# Authentication

> To authorize, use this code:

```python
import asyncio
from thingsdb.client import Client

client = Client()
loop = asyncio.get_event_loop()


async def example():
    # replace `localhost` with your ThingsDB server address
    await client.connect('localhost', 9200)

    # replace `amdin` with yout username and `pass` with your password
    await client.authenticate('admin', 'pass')

# run the example
loop.run_until_complete(example())

# the will close the client in a nice way
client.close()
loop.run_until_complete(client.wait_closed())
```

```shell
thingscmd -u admin -p pass -s localhost -c << EOL
/* Creates a new collection */
new_collection('awesome_things');
EOL
```

ThingsDB uses a user and password combination for access. A default user `admin` with password `pass` is created on a fresh installation.
If you did not yet change the default password, you might want to jump to [set password](#set-password)

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

# Events
When a query uses a statement which makes a change to ThingsDB, then internally ThingsDB will create an *event* to apply these changes.
Events are applied in order on each node so database consistency is guaranteed.

# Names
The following rules apply to names in ThingsDB:

- A name must start with a letter or underscore character
- A name cannot start with a number
- A name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Names are case-sensitive (thing, Thing and THING are three different names)
