---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - python: Python
  - shell: ThingsCMD
  # - curl: cURL

toc_footers:
  - Source on <a href='https://github.com/thingsdb/ThingsDocs'>GitHub</a>

includes:
  - operators
  - types
  - manage_api
  - r_collection
  - r_collections
  - r_counters
  - r_del_collection
  - r_del_user
  - r_grant
  - r_new_collection
  - r_new_node
  - r_new_user
  - r_node
  - r_nodes
  - r_pop_node
  - r_rename_collection
  - r_rename_user
  - r_reset_counters
  - r_revoke
  - r_set_password
  - r_set_quota
  - r_set_zone
  - r_shutdown
  - r_user
  - r_users
  - collection_api
  - c_blob
  - c_del
  - c_find
  - c_get
  - c_hasattr
  - c_hasprop
  - c_id
  - c_int
  - c_isarray
  - c_isascii
  - c_isbool
  - c_isfloat
  - c_isinf
  - c_isint
  - c_islist
  - c_isnan
  - c_isstr
  - c_istuple
  - c_isutf8
  - c_lower
  - c_map
  - c_now
  - c_pop
  - c_push
  - c_refs
  - c_rename
  - c_ret
  - c_set
  - c_splice
  - c_startswith
  - c_str
  - c_t
  - c_test
  - c_try
  - c_unset
  - c_upper
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
    # replace `node.local` with your ThingsDB server address
    await client.connect('node.local', 9200)

    # replace `amdin` with yout username and `pass` with your password
    await client.authenticate('admin', 'pass')

# run the example
loop.run_until_complete(example())

# the will close the client in a nice way
client.close()
loop.run_until_complete(client.wait_closed())
```

```shell
thingscmd -n node.local -u admin -p pass -c << EOL
/* Creates a new collection */
new_collection('awesome_things');
EOL
```



ThingsDB uses a user and password combination for access. A default user `admin` with password `pass` is created on a fresh installation.
If you did not yet change the default password, you might want to jump to [set password](#set_password)

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

# Properties

# Attributes

# Temporary variable

> This code uses a temporary variable:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        $tmp = 'This is a ';
        $tmp += 'temporary variable!!!';
        $tmp;
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
# note that we need to escape the $ sign in bash
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
\$tmp = 'This is a ';
\$tmp += 'temporary variable!!!';
\$tmp;
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    null,
    "This is a temporary variable!!!"
]
```

Can be used to assign a value to a variable which can be used within a query.

A temporary variable can be used withing the scope of a query and is automatically
destroyed after the query is finished.

To create a temporary variable, start with a dollar `$` sign, followed with a valid [name](#names).

Some valid examples:

- `$_ = ...`
- `$tmp = ...`
- `$var1 = ...`

<aside class="notice">
It is possible to re-assign or change a temporary variable within a query, as long as the variable
is not in use within the statement, for example:
<p><code>$tmp = [1, 2]; $tmp.map(_ => $tmp = nil);</code></p>
<p>...will raise a <code>BAD_REQUEST</code> <i>(cannot assign a new value to `$tmp` while the variable is in use)</i></p>
</aside>
