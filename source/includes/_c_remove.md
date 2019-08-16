## remove (list)

> This code shows an example using ***remove()*** on a list:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        $tmp = [1, 2, 3, 4];
        [
            $tmp.remove(|x| (x % 2 == 0)),
            $tmp,
        ];
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q  << EOQ "
\$tmp = [1, 2, 3, 4];
[
    \$tmp.remove(|x| (x % 2 == 0)),
    \$tmp,
];
"
EOQ
```

> Return value in JSON format

```json
[
    2,
    [
        1,
        3,
        4
    ]
]
```

This function removes and returns the value of the *first* element in the [array](#array-type)
that satisfies the callback function.
Otherwise `nil` is returned unless an alternative return value is specified.

This function generates an [event](#events).

### Function
*list*.`remove(callback, [alt])`

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


## remove (set)

> This code shows an example using ***remove()*** on a set:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        $t1 = {x:1}; $t2 = {x:2}; $t3 = {x:3}; $t4 = {x:4};
        $s = set([$t1, $t2, $t3, $t4]);
        [
            $s.remove(|t| (t.x < 3)),
            $s.remove($t1, $t2, $t3, $t4),
        ]
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -d 3 -q  << EOQ "
\$t1 = {x:1}; \$t2 = {x:2}; \$t3 = {x:3}; \$t4 = {x:4};
\$s = set([\$t1, \$t2, \$t3, \$t4]);
[
    \$s.remove(|t| (t.x < 3)),
    \$s.remove(\$t1, \$t2, \$t3, \$t4),
]
"
EOQ
```

> Example return value in JSON format

```json
[
    [
        {
            "#": 0,
            "x": 1
        },
        {
            "#": 0,
            "x": 2
        }
    ],
    [
        {
            "#": 0,
            "x": 3
        },
        {
            "#": 0,
            "x": 4
        }
    ]
]
```

This function can be used to remove `things` from a `set`.

If a closure is used, then all things that satisfy the test are removed from the set
and returned as list. The order of the removed things is not guaranteed since the set itself
is unordered.

It is also possible to specify `things` as arguments. In this case a list is returned with
all the things which are removed from the set, in the order that the arguments are used.
Things which are not found in the set are ignored.

This function generates an [event](#events).

### Function
*set*.`remove(callback)`

Or

*set*.`remove(thing1, thing2, ..., thingX)`

### Arguments
Explanation of the *callback* argument:

Iterable | Arguments | Description
-------- | -------- | -----------
set | thing, thing ID | Iterate over things in the set. Both `thing` and `thing ID` are optional.

### Return value
A list with the removed `things` from the set or an empty list if nothing is removed.
