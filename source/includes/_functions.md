# Query Collections

> This code returns the *id* of collection *stuff*

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('server.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query('id()', target='stuff')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -s server.local -u admin -p pass -c stuff -q 'id()'
```

## blob

> This code assigns the ThingsDB logo to an attribute *logo* using a blob:

```python
import asyncio
import urllib
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('server.local', 9200)
    await client.authenticate('admin', 'pass')
    stuff = await client.get_collection('stuff')

    # TODO: replace with ThingsDB logo
    resp = urllib.request.urlopen(
        'https://upload.wikimedia.org/wikipedia/commons/1/15/Siridb-logo.svg')

    # The python client will automatically use a blob for byte values
    await stuff.set('logo', resp.read())

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Note: thingscmd supports only one blob per query, so this is always blob(0)
wget 'https://upload.wikimedia.org/wikipedia/commons/1/15/Siridb-logo.svg' | \
thingscmd -s server.local -u admin -p pass -c stuff -q "set('logo', blob(0));"
```

Blobs can be used to send binary data to ThingsDB. Each query request allows you to send
an array of *blob* values together with the query. Within the query it is then possible
to use this function to *get* the blob value.

This function does *not* generate an [event](#events).

### Function
`blob(index);`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
index | int (required) | Index of a blob in the blobs array. This value may be negative, for example: `-1` can be used to get the last blob in the array.

### Return value
Returns the blob. An `INDEX_ERROR` is returned
if the blob at the given `index` does not exist.


## hasattr

This function does *not* generate an [event](#events).

## del

This function generates an [event](#events).

## endswith

Determines if a string ends with characters given by another string.

This function does *not* generate an [event](#events).

## filter

This function does *not* generate an [event](#events).

## find

This function does *not* generate an [event](#events).

## get

This function does *not* generate an [event](#events).

## hasprop

This function does *not* generate an [event](#events).

## id

This function does *not* generate an [event](#events).

## int

This function does *not* generate an [event](#events).

## isinf

This function does *not* generate an [event](#events).

## isnan

This function does *not* generate an [event](#events).

## lower

Return a new string in which all case-based characters are in lower case.

This function does *not* generate an [event](#events).

## map

This function does *not* generate an [event](#events).

## match

Determines if a string matches a given regular expression.

This function does *not* generate an [event](#events).

## now

This function does *not* generate an [event](#events).

## push

This function generates an [event](#events).

## rename

This function generates an [event](#events).

## ret

> This code pushes a value to an array but returns simple `nil`:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('server.local', 9200)
    await client.authenticate('admin', 'pass')
    stuff = await client.get_collection('stuff')

    # The python client adds ret() automatically
    await stuff.some_array.ti_push('something')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -s server.local -u admin -p pass -q << EOQ "
#
some_array.push('something').ret();
"
EOQ
```

> Return value in json format

```json
null
```

Use this function to simply return `nil`. This can be useful in some cases
where you don't want to return the default value from some function to prevent
unnecessary network traffic.

This function does *not* generate an [event](#events).

### Function
`ret();`

### Return value
Returns `nil`.


## set

This function generates an [event](#events).

## splice

This function does *not* generate an [event](#events).

## startswith

Determines if a string starts with characters given by another string.

This function does *not* generate an [event](#events).

## str

This function does *not* generate an [event](#events).

## thing

This function does *not* generate an [event](#events).

## unset

This function generates an [event](#events).

## upper

Return a new string in which all case-based characters are in upper case.

This function does *not* generate an [event](#events).
