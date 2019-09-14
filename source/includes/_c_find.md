## find

> This code shows an example using ***find()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('localhost')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        users.find(|user| user.name.startswith('Jeroen'));
    ''', scope='@:stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n localhost -u admin -p pass -s @:stuff -q << EOQ "
users.find(|user| user.name.startswith('Jeroen'));
"
EOQ
```

> Example return value in JSON format

```json
{
    "#": 16,
    "email": "jeroen@transceptor.technology",
    "name": "Jeroen van der Heijden"
}
```

This function returns the value of the first element in the [array](#array-type) or [set](#set-type) that satisfies the callback function.
Otherwise `nil` is returned unless an alternative return value is specified.

This function does *not* generate an [event](#events).

<aside class="notice">
The return value when called on a <code>set</code> might be unpredictable since a set is not ordered.
<p><code>set([{name: 'Iris'}, {name: 'Cato'}]).find(||true);</code></p>
<p>...will return <code>{Iris}</code> <i>or</i> <code>{Cato}</code>.</p>
</aside>


### Function
*iterable*.`find(callback, [alt])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each value until the closure evaluates to true.
alt | any (optional) | Alternative value which is returned if no item has passed the *callback* test.

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
array    | item, index | Iterate over items in the array. Both `item` and `index` are optional.
set      | thing, id   | Iterate over things in the set. Both `thing` and `id` are optional.

<aside class="notice">
The <code>alt</code> argument will be <i>lazy</i> evaluated. Consider the following example:
<p><code>elems.find(|e| (e.name == "foo"), items.pop());</code><p>
Here, the item will <i>only</i> be popped, in case <code>e</code> with <code>name</code> <i>foo</i> is <i>not</i> found in <code>elems</code>.
</aside>

### Return value
The value of the first element in the array or thing that satisfies the provided testing function;
otherwise, `nil` or a specified alternative value is returned.
