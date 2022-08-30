---
title: "str"
weight: 123
---

This is the `string` type of ThingsDB. A value of type `str` *should* contain valid UTF-8 characters. This
is not guaranteed but rather depends on [MessagePack](https://msgpack.org) to pack data correctly.
There is an [is_utf8](../../collection-api/is_utf8) function which can be used to test a `str` value for valid UTF-8
data and it is also possible to create an `utf8` property on a custom [Type](../../overview/type) which only allows strings
with valid UTF-8 data.

### Functions

Function | Description
------ | -----------
[contains](./contains) | Determine if a given string is a substring of a string.
[ends_with](./ends_with) | Determine if a string ends with characters given by another string.
[len](./len) | Return the length of a string.
[lower](./lower) | Return a new string in which all case-based characters are in lower case.
[replace](./replace) | Returns a new string in witch occurrences of a given substring or regular expression match are replaced with another substring.
[split](./split) | Split a string into a new list with substrings.
[starts_with](./starts_with) | Determine if a string starts with characters given by another string.
[trim](./trim) | Returns a new string with whitespace characters removed from both the *start* and *end* of a string.
[trim_left](./trim_left) | Returns a new string with whitespace characters removed from the *start* of a string.
[trim_right](./trim_right) | Returns a new string with whitespace characters removed from the the *end* of a string.
[upper](./upper) | Return a new string in which all case-based characters are in upper case.

> This code creates a *raw* property *greet* to collection *stuff*:

```thingsdb,should_pass
.greet = 'Hello world!!';
```
