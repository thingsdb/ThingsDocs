## remove

> This code shows an example using ***remove()***:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        ( $tmp = [1, 2, 3, 4] ).ret();
        $tmp.remove(|x| (x % 2 == 0));
        $tmp;
    ''', target='stuff', all_=True)
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -a -q  << EOQ "
( \$tmp = [1, 2, 3, 4] ).ret();
\$tmp.remove(|x| (x % 2 == 0));
\$tmp;
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    2,
    [
        1,
        3,
        4
    ]
]
```

This function removes and returns the value of the first element in the [array](#array) that satisfies the callback function.
Otherwise `nil` is returned unless an alternative return value is specified.

This function generates an [event](#events).

### Function
*mutable_array*.`remove(callback, [alt])`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
callback | closure | Closure to execute on each value until the closure evaluates to true.
alt | any (optional) | Alternative value which is returned if no item has passed the *callback* test.

Explanation of the *callback* argument:

Iterable | Arguments | Description
-------- | -------- | -----------
array | item, index | Iterate over items in the array. Both item and index are optional.

<aside class="notice">
The <code>alt</code> argument will be <i>lazy</i> evaluated. Consider the following example:
<p><code>elems.remove(|e| (e.name == "foo"), items.pop());</code><p>
Here, the item will <i>only</i> be popped, in case <code>e</code> with <code>name</code> <i>foo</i> is <i>not</i> found in <code>elems</code>.
</aside>

### Return value
The value of the first element in the array or thing that satisfies the provided testing function;
otherwise, `nil` or a specified alternative value is returned.
