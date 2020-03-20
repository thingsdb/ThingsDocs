---
title: "int"
weight: 40
---

ThingsDB can store 64bit signed integer values. When assigning integer values
larger than 64bit, an [overflow_err()](../../errors/overflow_err) will be returned. Other types can be
converted to `int` by using the [int](../../collection-api/int) function.

### Notations

Base | Example | Description
---- | ------- | -----------
2 | `0b1111011` | Binary notation starts with `0b` (zero, lower case `b`), followed by binary digits (`0-1`).
8 | `0o173` | Octal notation starts with `0o` (zero, lower case `o`), followed by octal digits (`0-8`).
10 | `123` | Decimal notation, numbers between zero and nine (`0-9`).
16 | `0x7b` | Hexadecimal notation start with a `0x` (zero, lower case `x`), followed by hexadecimal digits (`0-9`, `a-f` or `A-F`).

> This code creates a *int* property *count* to collection *stuff*:

```thingsdb,should_pass
.count = 123;
```
