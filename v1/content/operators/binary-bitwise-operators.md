---
title: "Binary bitwise operators"
weight: 164
---

Can be used on [integer](../../data-types/int) values.

Operator | Description
-------- | -----------
`&` | Bitwise AND, `true` if both `a` and `b` are `1`.
`|` | Bitwise OR, `true` if at least `a` or `b` is `1`.
`^` | Bitwise XOR, `true` if `a` and `b` are different.

> Binary bitwise operator examples:

```thingsdb,json_response
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
