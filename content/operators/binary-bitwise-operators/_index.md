---
title: "Binary bitwise operators"
date: 2019-10-14T09:34:41+02:00
weight: 3
---

Can be used on [integer](../../data-types/integer) values.

Operator | Description
-------- + -----------
`&` | Bitwise AND, `true` if both `a` and `b` are `1`.
<code>&#124;</code> | Bitwise OR, `true` if at least `a` or `b` is `1`.
`^` | Bitwise XOR, `true` if `a` and `b` are different.

> Binary bitwise operator examples:

```
[
    0b110 & 0b011,
    0b110 | 0b011,
    0b110 ^ 0b011,
];
```

> Return value in JSON format

```json
[
    2,
    7,
    5
]
```
