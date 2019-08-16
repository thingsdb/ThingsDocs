# Data Types
ThingsDB has some basic

## Nil

 > This code uses `nil` to prevent returning unused data:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''
        my_array = [1, 2, 3, 42];
        nil;  /* without nil, the array above would be returned */
    ''', target='stuff')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
my_array = [1, 2, 3, 42];
nil;  /* without nil, the array above would be returned */
"
EOQ
```

Probably the most simple type, it can be used as *no value*.

It might be useful to use `nil` as the last statement in a query to prevent
returning data which is not required. See the code example.

## String (raw)

 > This code creates a *raw* property *greet* to collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''

        greet = 'Hello world!!';

    ''', target='stuff')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "

greet = 'Hello world!!';

"
EOQ
```

ThingsDB has only type `raw` which is used for storing both *strings* and *blob* values.

### Methods
Method | Description
------ | -----------
[endswith](#endswith) | Determines if a string ends with characters given by another string.
[len](#len) | Returns the length of a string.
[lower](#lower) | Return a new string in which all case-based characters are in lower case.
[startswith](#startswith) | Determines if a string starts with characters given by another string.
[test](#test) | Test if a string matches a given regular expression and return `true` or `false`.
[upper](#upper) | Return a new string in which all case-based characters are in upper case.


## Boolean

> This code creates a *bool* property *is_the_earth_flat* to collection *stuff*:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])

    res = await client.query(r'''

        is_the_earth_flat = !true;

    ''', target='stuff')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
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
    await client.authenticate(auth=['admin', 'pass'])
    res = await client.query(r'''

        count = 123;

    ''', target='stuff')
    print(res)

asyncio.get_event_loop().run_until_complete(example())
```

```shell
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
    await client.authenticate(auth=['admin', 'pass'])
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

ThingsDB uses 64bit to store float values and has support for the `e` notation and
special *float* values like `inf`, `-inf` and `nan`.

### Useful methods

Method | Description
------ | -----------
[float](#float) | return a float type for a given value.
[isfloat](#isfloat) | check if the given value is of the float type.
[isinf](#isinf) | check if the given value is infinite.
[isnan](#isnan) | check if the given value is not-a-number.

## Regex

> This code uses a regular expression for an overly simple email check:

```python
import asyncio
from thingsdb.client import Client

client = Client()

async def example():
    await client.connect('node.local')
    await client.authenticate(auth=['admin', 'pass'])

    # Note: the email check is oversimplified, do not use in production
    await client.query(r'''
        email_test = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;

        /* example usage of our 'email_test' */
        $email = 'info@thingsdb.net';
        $email.test( email_test );
    ''', target='stuff')

asyncio.get_event_loop().run_until_complete(example())
```

```shell
# Note: the email check is oversimplified, do not use in production
thingscmd -n node.local -u admin -p pass -c stuff -q << EOQ "
email_test = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;

/* example usage of our 'email_test' */
\$email = 'info@thingsdb.net';
\$email.test( email_test );
"
EOQ
```

> Return value in JSON format

```json
true
```

Regular expression can be constructed using a literal which consists of a pattern enclosed between slashes, as follows: `re = /ab+c/;`.
It is probably a good idea to store a `regex` in a variable if you plan to use the regular expression multiple times. This prevents the
requirement to compile the regular expression each time.

### Methods that use regular expressions
Method | Description
------ | -----------
[test](#test) | A [string](#string-raw) method that tests for a match in a string. It returns `true` or `false`.


## Array type

An empty array can be constructed as follows: `arr = [];`

Nesting is also possible withing but each nested array will become a `tuple` which means the array will be immutable.
ThingsDB does this because it wants to update all changes to subscribers and finds the subscribers by the parent object where
the change is  made. Since the parent of a nested array is another array, the `thing` holding the array would not be found.

Another *weird* property of ThingsDB is that `arrays` are always *copies*, and not by *reference* as in most languages. This is
because ThingsDB needs to know which subscribers to update with changes made to the `array`.


### Methods
Method | Description
------ | -----------
[filter](#filter) | Returns a new `array` with elements that pass a given test.
[find](#find) | Returns the first element that pass a given test.
[findindex](#findindex) | Returns the index of the first element that pass a given test.
[indexof](#indexof) | Returns the index of a given value, or `nil` if not found.
[len](#len) | Returns the length of the array.
[map](#map) | Returns a new `array` with the results of calling a provided closure on every element.
[pop](#pop) | Removes the last element from an array and returns that element.
[push](#push) | Adds new items to the end of an array, and returns the new length.
[remove](#remove-list) | Removes the first element that pass a given test and returns that element.
[splice](#splice) | Determines if a string starts with characters given by another string.


### Array Types

Type | Description
---- | -----------
list | Mutable array.
tuple | Immutable array, *nested* arrays are always tuples.

<aside class="notice">
It is not possible to change an array while the array is in use, for example:
<p><code>$tmp = [1, 2, 3]; $tmp.map(|i| $tmp.push(i));</code></p>
<p>...will raise <code>BAD_REQUEST</code> <i>(cannot use function `push` while the array is in use)</i></p>
</aside>


## Thing

### Methods
Method | Description
------ | -----------
[del](#del) | Remove a property.
[filter](#filter) | Return a new `thing` with properties that pass a given test.
[id](#id) | Return the `id`.
[len](#len) | Returns the number of items.
[map](#map) | Returns an [array](#array-type) with the results of calling a provided closure on every item.


## Closure

Closures can be used to consume items from a `thing`, `array` or `set`.

<aside class="notice">
It is not possible to use closures with recursion, for example:
<p><code>$a = ||map($a); map($a);</code></p>
<p>...will raise <code>BAD_REQUEST</code> <i>(closures cannot be used recursively)</i></p>
</aside>


## Set type

A set is a collection which is unordered and can only contain things.
Each [thing](#thing) will only exists once in a collection.

### Methods
Method | Description
------ | -----------
[add](#add) | Add things to a set.
[filter](#filter) | Return a new `set` with things that pass a given test.
[find](#find) | Returns the first `thing` which passes a given test.
[has](#has) | Test if a set contains a given thing.
[map](#map) | Return an [array](#array-type) with the results of calling a provided closure on every thing.
[remove](#remove-set) | Remove things from a set.
[set](#set) | Create a new empty set or convert an [array](#array-type) to a new set.

## Error type


### Related functions
Method | Description
------ | -----------
[err](#err) | Initialize a new error.
[raise](#raise) | Raise an error.
[try](#try) | Try a statement and catch if an error is raised.

