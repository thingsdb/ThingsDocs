## assert

> This code shows how assert can be used:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    # evaluate 1 > 2 with an assert message
    res = await client.query(r'''
        assert(1 > 2, 'one is still smaller than two');
    ''', scope='@:stuff')
    print(res)
    # Error code is set: `res.error_code == 1`

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
assert(1 > 2, 'one is still smaller than two');
"
EOQ
```

> Returns with an  `ASSERTION_ERROR` exception

```json
{
    "error_msg": "one is still smaller than two",
    "error_code": 1
}
```

Raises `ASSERTION_ERROR` if the specified statement evaluates to `false`.

This function does *not* generate an [event](#events).


### Function
`assert(statement [, error_msg])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
statement | any (required) | The statement to evaluate.
msg | raw (optional) | Custom error message.
code | int (optional) | Return a custom error code between 1 and 32. If not given, the error code is `ASSERTION_ERROR` (-105)

### Return value
Assert returns with the return value of the given statement when the statement evaluates to `true`. Otherwise
an `ASSERTION_ERROR` is raised.