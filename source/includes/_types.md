# Data Types
ThingsDB has some basic

## String/Raw

 > This code creates a *raw* property *greet* to collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('server.local', 9200)
    await client.authenticate('admin', 'pass')
    # get collection `stuff`
    collection = await client.get_collection('stuff')

    # assign property `greet`
    await collection.assign('greet', 'Hello world!!')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -u admin -p pass -s server.local -c stuff -q << EOQ "
greet = 'Hello world!!';
"
EOQ
```

ThingsDB has only type `raw` which is used for storing both *strings* and *blob* values.

### Methods
Method | Description
------ | -----------
[upper](#upper) | Return a new string in which all case-based characters are in upper case.

<aside class="notice">
If you want to store long string or blob values, you might want to use
<code>attributes</code> rather than <code>properties</code>. Attributes take less
memory then properties but the downside is that it is not possible to search within
a value. (unless you *download* the value first.)
</aside>

## Integer


## Boolean


