# Operators

## Binary bitwise operators

> Binary bitwise operator examples:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        (0b110 & 0b011);
        (0b110 | 0b011);
        (0b110 ^ 0b011);
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
(0b110 & 0b011);
(0b110 | 0b011);
(0b110 ^ 0b011);
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    2,
    7,
    5
]
```

Can be used on [integer](#integer) values.

Operator | Description
-------- + -----------
`&` | Bitwise AND, `true` if both `a` and `b` are `1`.
<code>&#124;</code> | Bitwise OR, `true` if at least `a` or `b` is `1`.
`^` | Bitwise XOR, `true` if `a` and `b` are different.


## Arithmetic operators

> Arithmetic examples:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        ( 5 + 2 );
        ( 5 - 2 );
        ( 5 / 2 );
        ( 5 // 2 );
        ( 5 * 2 );
        ( 5 % 2 );
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
( 5 + 2 );
( 5 - 2 );
( 5 / 2 );
( 5 // 2 );
( 5 * 2 );
( 5 % 2 );
"
EOQ
```

> Return value in JSON format

```json
[
    7,
    3,
    2.5,
    2,
    10,
    1
]
```

Operator | Description
-------- | -----------
`+` | Addition operator.
`-` | Subtraction operator.
`/` | Float division operator.
`//` | Integer division operator.
`*` | Multiplication operator.
`%` | Modulo operator.


## Assignments

Assignments will generate an [event](#events).

Operator | Description
-------- | -----------
`=` | Assignment operator.
`*=` | Multiplication assignment.
`/=` | Float division assignment.
`//=` | Integer division assignment.
`%=` | Modulo assignment.
`+=` | Addition assignment.
`-=` | Subtraction assignment
`&=` | Bitwise AND assignment.
`^=` | Bitwise XOR assignment.
<code>&#124;=</code> | Bitwise OR assignment.

## Logical operators

> Logical *short-circuit* examples:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    # Note: x += 1 never is executed
    res = await client.query(r'''
        x = 0;
        (false && x += 1);
        (true || x += 1);
        x;
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Note: x += 1 never is executed
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
x = 0;
(false && x += 1);
(true || x += 1);
x;
"
EOQ
```

> Return value in JSON format

```json
[
    null,
    false,
    true,
    0
]
```

Logical operators are typically used with [boolean](#boolean) values.

Operator | Description
-------- | -----------
`&&` | Logical AND.
<code>&#124;&#124;</code> | Logical OR.

As logical expressions are evaluated left to right, they are tested for possible *"short-circuit"* evaluation using the following rules:

- `(some falsy expression) && expr` is short-circuit evaluated to the falsy expression;
- `(some truthy expression) || expr` is short-circuit evaluated to the truthy expression.

Short circuit means that the `expr` parts above are not evaluated, hence any side effects of doing so do not take effect
(e.g., if expr is a function call, the calling never takes place).
This happens because the value of the operator is already determined after the evaluation of the first operand.


## Conditional (ternary) operator

> Conditional (ternary) operator examples:

```python
import asyncio
from thingsdb.client import Client

async def example():
    await client.connect('node.local', 9200)
    await client.authenticate('admin', 'pass')
    res = await client.query(r'''
        ( 2 > 1 ) ? 'two is larger than one' : 'two is NOT larger than one';
    ''', target='stuff')
    print(res)

client = Client()
asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
( 2 > 1 ) ? 'two is larger than one' : 'two is NOT larger than one';
"
EOQ
```

> Return value in JSON format

```json
"two is larger than one"
```

The conditional operator returns one of two values based on the logical value of the condition.

### Syntax:
`(condition) ? if-true : if-false`
