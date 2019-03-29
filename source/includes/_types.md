# Data Types
ThingsDB has some basic

## Nil

Probably the most simple type, it's used as *no value*.
What more can we say about `nil`?


## String / Raw

 > This code creates a *raw* property *greet* to collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    # Get collection `stuff`
    stuff = await client.get_collection('stuff')

    # Assign property `greet`
    await stuff.assign('greet', 'Hello world!!')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Assign property `greet`
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
greet = 'Hello world!!';
"
EOQ
```

ThingsDB has only type `raw` which is used for storing both *strings* and *blob* values.

### Methods
Method | Description
------ | -----------
[endsswith](#endsswith) | Determines if a string ends with characters given by another string.
[lower](#lower) | Return a new string in which all case-based characters are in lower case.
[startswith](#startswith) | Determines if a string starts with characters given by another string.
[test](#test) | Test if a string matches a given regular expression and return `true` or `false`.
[upper](#upper) | Return a new string in which all case-based characters are in upper case.

<aside class="warning">
If you want to store long string or blob values, you might want to use
<code>attributes</code> rather than <code>properties</code>. Attributes take less
memory then properties but the downside is that it is not possible to search within
a value. (unless you *download* the value first.)
</aside>


## Boolean

> This code creates a *bool* property *is_the_earth_flat* to collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    # Get collection `stuff`
    stuff = await client.get_collection('stuff')

    # Assign property `is_the_earth_flat`
    await stuff.assign('is_the_earth_flat', not True)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Assign property `is_the_earth_flat`
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
is_the_earth_flat = !true;
"
EOQ
```

Boolean are either `true` or `false`.
Other types can convert to `bool` by using the `!` (not) operator or the [bool](#bool) function.


## Integer

 > This code creates a *int* property *count* to collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    # Get collection `stuff`
    stuff = await client.get_collection('stuff')

    # Assign property `count`
    await stuff.assign('count', 123)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Assign property `count`
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
count = 123;
"
EOQ
```

ThingsDB can store 64bit signed integers values. When assigning integer values
larger than 64bit, an `OVERFLOW_ERROR` will be returned. Other types can be
converted to `int` by using the [int](#int) function.

### Notations

Base | Example | Description
---- | ------- | -----------
2 | `0b1111011` | Binary notation starts with `0b` (zero, lower case `b`), followed by binary digits (`0-1`).
8 | `0o173` | Octal notation starts with `0o` (zero, lower case `o`), followed by octal digits (`0-8`).
10 | `123` | Decimal notation, numbers between zero and nine (`0-9`).
16 | `0x7b` | Hexadecimal notation start with a `0x` (zero, lower case `x`), followed by hexadecimal digits (`0-9`, `a-f` or `A-F`).

## Floating point

 > This code creates a *float* property *plank_constant* to collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')
    # Get collection `stuff`
    stuff = await client.get_collection('stuff')

    # Assign property `plank_constant`
    await stuff.assign('plank_constant', 6.62607004e-34)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Assign property `plank_constant`
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
plank_constant = 6.62607004e-34;
"
EOQ
```

ThingsDB can store 64bit float values.  [isinf](#isinf) and [isnan](#isnan)


## Regex

> This code uses a regular expression for an overly simple email check:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate('admin', 'pass')

    # Note: the email check is oversimplified, do not use in production
    await client.query(r'''
        email = 'info@thingsdb.net';
        email.test( /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/ );
    ''', target='stuff')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Note: the email check is oversimplified, do not use in production
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
email = 'info@thingsdb.net';
email.test( /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/ );
"
EOQ
```

> Return value in JSON format (the first `nil` is for the email assignments)

```json
[
    null,
    true
]
```

Regular expression can be constructed using a literal which consists of a pattern enclosed between slashes, as follows: `re = /ab+c/;`.

### Methods that use regular expressions
Method | Description
------ | -----------
[test](#test) | A [string](#string-raw) method that tests for a match in a string. It returns `true` or `false`.


## Array

An empty array can be constructed as follows: `arr = [];`

Nesting is also possible withing but each nested array will become a `tuple` which means the array will be immutable.
ThingsDB does this because it wants to update all changes to subscribers and finds the subscribers by the parent object where
the change is  made. Since the parent of a nested array is another array, the `thing` holding the array would not be found.

Another *weird* property of ThingsDB is that `arrays` are always *copies*, and not by *reference* as in most languages. This is
because ThingsDB needs to know which subscribers to update with changes made to the `array`.


### Methods
Method | Description
------ | -----------
[filter](#filter) | Return a new `array` with elements that pass a given test.
[find](#find) | Returns the first element for which a given test passes.
[findindex](#findindex) | Returns the index of the first element which passes given test.
[indexof](#indexof) | Returns the index of a given value, or `nil` if .
[remove](#remove) | Remove the  by value.
[splice](#splice) | Determines if a string starts with characters given by another string.
[pop](#pop) | Removes the last element from an array and returns that element.
[push](#push) | Adds new items to the end of an array, and returns the new length.


### Array Types

Type | Description
---- | -----------
list | Mutable array.
tuple | Immutable array, *nested* arrays are always tuples.

<aside class="notice">
It is not possible to change an array while the array is in use, for example:
<p><code>$tmp = [1, 2, 3]; $tmp.map(i => $tmp.push(i));</code></p>
<p>...will raise <code>BAD_REQUEST</code> <i>(cannot use function `push` while the array is in use)</i></p>
</aside>


## Thing


## Closure

