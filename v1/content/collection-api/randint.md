---
title: "randint"
weight: 255
---

Returns **pseudo-random** [integer](../../data-types/int) number between a given range.

The first argument specifies the *start* of the range and must have a value *less* than the
second argument when specifies the *end* of the range. The *start* is *inclusive* and the *end* is
*exclusive*, for example: `randint(0, 2)` will return either `0` or `1`.

{{% notice warning %}}
Do not use **randint()** when the purpose is security related since the linear
congruential algorithms used by this function are too easy to break.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`randint(start, end)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`start` | int (required) | Start of the range **(inclusive)**.
`end` | int (required) | End of the range **(exclusive)**.

### Return value

A pseudo-random [int](../../data-types/int) between `start` (inclusive) and `end` (exclusive).

### Example

> Example on how ***randint(..)*** can be used:

```thingsdb,should_pass
// Return a pseudo-random number between 10 (inclusive) and 20 (exclusive)
randint(10, 20);
```

Example return value in JSON format:

```json
13
```
