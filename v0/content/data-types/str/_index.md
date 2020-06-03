---
title: "str"
weight: 77
---

This is the `string` type of ThingsDB. A value of type `str` *should* contain valid UTF-8 characters. This
is not guaranteed but rather depends on [MessagePack](https://msgpack.org) to pack data correctly.
There is an [isutf8](../../collection-api/isutf8) function which can be used to test a `str` value for valid UTF-8
data and it is also possible to create an `utf8` property on a custom [Type](../type) which only allows strings
with valid UTF-8 data.

### Functions

Function | Description
------ | -----------
[contains](./contains) | Determine if a given string is a substring of a string.
[endswith](./endswith) | Determine if a string ends with characters given by another string.
[len](./len) | Return the length of a string.
[lower](./lower) | Return a new string in which all case-based characters are in lower case.
[startswith](./startswith) | Determine if a string starts with characters given by another string.
[test](./test) | Test if a string matches a given regular expression and return `true` or `false`.
[upper](./upper) | Return a new string in which all case-based characters are in upper case.

> This code creates a *raw* property *greet* to collection *stuff*:

```thingsdb,should_pass
.greet = 'Hello world!!';
```
