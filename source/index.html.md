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
  - node_api
  - n_counters
  - n_node
  - n_nodes
  - n_reset_counters
  - n_set_loglevel
  - n_set_zone
  - n_shutdown
  - thingsdb_api
  - r_collection
  - r_collections
  - r_del_collection
  - r_del_user
  - r_grant
  - r_new_collection
  - r_new_node
  - r_new_user
  - r_pop_node
  - r_rename_collection
  - r_rename_user
  - r_replace_node
  - r_revoke
  - r_set_loglevel
  - r_set_password
  - r_set_quota
  - r_set_zone
  - r_shutdown
  - r_user
  - r_users
  - collection_api
  - c_add
  - c_assert
  - c_blob
  - c_bool
  - c_del
  - c_filter
  - c_find
  - c_findindex
  - c_has
  - c_hasprop
  - c_id
  - c_indexof
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
  - c_isthing
  - c_istuple
  - c_isutf8
  - c_len
  - c_lower
  - c_map
  - c_now
  - c_pop
  - c_push
  - c_refs
  - c_remove
  - c_rename
  - c_ret
  - c_set
  - c_splice
  - c_startswith
  - c_str
  - c_t
  - c_test
  - c_try
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
    await client.connect('node.local')

    # replace `amdin` with yout username and `pass` with your password
    await client.authenticate('admin', 'pass')

# run the example
loop.run_until_complete(example())

# the will close the client in a nice way
client.close()
loop.run_until_complete(client.wait_closed())
```

```shell
thingscmd -n node.local -u admin -p pass -q << EOL
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

# Query

> Example query

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect(
        'node.local',       # node address
        9200                # node port, default 9200
    )
    await client.authenticate(
        'admin',            # username
        'pass'              # password
    )
    res = await client.query(
        "'Hello world!!'",  # query string
        target=client.node, # collection or scope, defaults to client.thingsdb
    )
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd \
    --node        node.local \
    --user        admin      \
    --password    pass       \
    --scope       node       \
    --query       "'Hello world!!'"
```

> Request in JSON format

```json
{
    "query": "'Hello world!!'",
    "collection": "stuff",
    "deep": 1,
    "blobs": []
}
```

Queries to ThingsDB can be used to manage [nodes](#node-api), [ThingsDB](#thingsdb-api) or to query [collections](#collection-api).

ThingsDB will respond with the last statement result, or, when `all` is set to `true`,
an array containing the results for each statement. In case a statement fails, the other statements are
not processed and an [error](#errors) is returned. Changes made are synchronized, even when an error has ocurred.

A query request has one required field *query*, and some other optionals:

Key | Type | Description
--- | ---- | -----------
`query` | string | The query string containing one or more statements. (required)
`target` | string| Target collection, or `0` for manage queries. (default: `0`)
`deep` | integer | Specify the depth in the range 0-127 to which `things` should be fully returned. (default: `1`)
`all` | boolean | When true, all statement results are returned in an array, otherwise only the last statement result. (default: `false`)
`blobs` | array | Additional blobs for binary data. (default: `[]`)

To send a query you can either use a language binding, see code examples, or if you
want to know how to serialize and send the data, read the [protocol](#protocol) section.

# Protocol
This is a more in depth view of the protocol used for communication with ThingsDB.
In case you just want to use ThingsDB using one of the language bindings, then this
info can be skipped. If you plan to implement you own connector, then this info might
be useful to you.

Communication with ThingsDB is done over a socket, either using TCP or a UNIX PIPE connection.
Once a connection is made, packages can be send to ThingsDB. Each package starts
with a 8 bytes header using little endian, followed by optional data. Before you can
send queries to ThingsDB, the connection must be authenticated. This can be done by
sending an `AUTH` package.

## Package

> Package format:

```
┌───────────┬───────────┬───────────┬───────────┬───────────┐
│ LEN (4)   │ ID (2)    │ TYPE (1)  │ CHK (1)   │ DATA (..) │
└───────────┴───────────┴───────────┴───────────┴───────────┘
```

### LEN (Unsigned, 32bit)
Length of the data, the header not included.

### ID (16bit)
The ID can be used as an identifier of your package. When ThingsDB send a response
on a request, it will use the same ID so this allows you to map a response to a
request. This is useful if you want to send multiple request in parallel.

### TYPE (Unsigned, 8bit)
Package type is used to describe what kind of package is transmitted.

#### Request type
Type | Number | Description
--------| -----| -----------
`PING`  | 32 | Ping, useful as keep-alive.
`AUTH`  | 33 | Authentication, expects: `[username, password]`
`QUERY_COLLECTION` | 36 | Query, see [query](#query) for more info.
`WATCH` | 48 | Watch, see [watch](#watch) for more info.
`UNWATCH` | 49 | Stop watching specified things, see [watch](#watch) for more info.

### CHK (Unsigned, 8bit)
Inverse of the type: `type ^ 0xff`, this is used as a check-bit.

### DATA
Data serialized using [qpack](https://github.com/transceptor-technology/libqpack).

## Example
As an example we create an authentication package for the default *admin* user with password *pass*.

This is the package data for our authentication request:

`["admin", "pass"]`

Serializing the above using *qpack* results in the following `12` bytes:

`\xef\x85admin\x84pass`

Now we create the header, for this example we just use ID 0:

- Data length (12) `\x0c\x00\x00\x00`
- Identifier (0) `\x00\x00`
- Auth package type (33) `\x21`
- Inverse type check bit (222) `\xde`


So our total package will be:

`\x0c\x00\x00\x00\x00\x00\x21\xde\xef\x85admin\x84pass`


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
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        $tmp = 'This is a temporary variable!!!';
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
# note that we need to escape the $ sign in bash
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
\$tmp = 'This is a temporary variable!!!';
"
EOQ
```

> Return value in JSON format

```json
"This is a temporary variable!!!"
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
<p><code>$tmp = [1, 2]; $tmp.map(|| $tmp = nil);</code></p>
<p>...will raise a <code>BAD_REQUEST</code> <i>(cannot assign a new value to `$tmp` while the variable is in use)</i></p>
</aside>
