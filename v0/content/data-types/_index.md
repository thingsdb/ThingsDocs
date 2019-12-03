---
title: "Data Types"
weight: 15
chapter: true
---

# Data Types

ThingsDB uses the following data types:

type | Description
------ | -----------
[bool](./bool) | Booleans are either `true` or `false`.
[bytes](./bytes) | Byte sequence.
[closure](./closure) | Closures can be used as functions or to consume items from a `thing`, `list`, `tuple` or `set`.
[error](./error) | An object containing information about an error.
[float](./float) | Floating point type.
[info](./info) | Return value for all `*_info()` functions.
[int](./int) | Integer type.
[list](./list) | Mutable array type.
[nil](./nil) | Used to define a null value, or no value at all.
[regex](./regex) | Regular expression.
[set](./set) | Unordered group of unique things.
[str](./str) | String type.
[thing](./thing) | Object with key value pairs.
[tuple](./tuple) | Nested and immutable [list](./list).
[Type](./type) | Type are [things](./thing) with pre-defined properties.
[&lt;Type&gt;](./wtype) | Wrapped thing by a [Type](./type).
