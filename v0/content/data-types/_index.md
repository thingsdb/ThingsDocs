---
title: "Data Types"
weight: 28
chapter: true
---

# Data Types

ThingsDB uses the following data types:

type | Description
------ | -----------
[bool](./bool) | Booleans are either `true` or `false`.
[bytes](./bytes) | Byte sequence.
[closure](./closure) | Closures can be used as functions or to consume items from a `thing`, `list`, `tuple` or `set`.
[datetime](./datetime) | Type `datetime` can be used to store a value with date and time information.
[enum](./enum) | Enumerators.
[error](./error) | An object containing information about an error.
[float](./float) | Floating point type.
[future](./future) | Futures can be used with modules and to postpone and isolate work.
[info](./info) | Return value of all `*_info()` functions.
[int](./int) | Integer type.
[list](./list) | Mutable array type.
[nil](./nil) | Used to define a null value, or no value at all.
[regex](./regex) | Regular expression.
[set](./set) | Unordered group of unique things.
[str](./str) | String type.
[thing](./thing) | Object with key value pairs.
[timeval](./timeval) | Like `datetime` but returns as a UNIX time-stamp by default.
[tuple](./tuple) | Nested and immutable [list](./list).
[Type](./type) | Type are [things](./thing) with pre-defined properties.
[&lt;Type&gt;](./wtype) | Wrapped thing by a [Type](./type).
