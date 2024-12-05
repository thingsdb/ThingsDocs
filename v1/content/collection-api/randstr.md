---
title: "randstr"
weight: 301
---

Returns a [string](../../data-types/str) with random characters.

The default characters to generate a string are URL-safe and contain the characters `0-9`, `A-Z`, `a-z`, `-` and `_`.

Instead of the default character set, it is possible to use your own set. This custom set may contain duplicated characters which increase the chance for certain characters to occur in the final string. For example, a random string based on the character set `AAB` will most likely contain more `A`'s than `B`'s.

{{% notice info %}}
This function is using the `SYS_getrandom` system call to generate random data and is therefore more secure compared to the other random functions in ThingsDB.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`randstr(length, [character-set])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`length` | int (required) | Length of the output string.
`character-set` | str (optional) | Custom character set, used to generate the output string.

### Return value

A random [string](../../data-types/str) of a given length.

### Example

> Some examples on how ***randstr(..)*** can be used:

```thingsdb,should_pass
// Returns a string of 16 random characters using the default character set.
randstr(16);
```

Example return value in JSON format:

```json
"kKoi4jZ-bFtc5Pwg"
```

```thingsdb,should_pass
// Returns a string of 10 random characters using only HEX characters
randstr(10, '0123456789ABCDEF');
```

Example return value in JSON format:

```json
"7AFBAE572B"
```
