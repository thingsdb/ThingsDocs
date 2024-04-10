---
title: "Binary bitwise operators"
weight: 195
---

Can be used on [integer](../../data-types/int) values.

Operator | Description
-------- | -----------
`&` | Bitwise AND, `true` if both `a` and `b` are `1`.
`\|` | Bitwise OR, `true` if at least `a` or `b` is `1`.
`^` | Bitwise XOR, `true` if `a` and `b` are different.
`~` | Bitwise NOT,  inverts each individual bit in the binary representation of a number. This means it creates a new number where every 0 becomes a 1, and every 1 becomes a 0.
`<<` | Left Shift, moves the bits of an integer to the left.
`>>` | Right Shift, moves the bits of an integer to the right.

> Binary bitwise operator examples:

```thingsdb,json_response
[
    0b110 & 0b011,  // 0b010 = 2
    0b110 | 0b011,  // 0b111 = 7
    0b110 ^ 0b011,  // 0b101 = 5
    ~5,             // Invert all individual bits
    1 << 4,         // 0b00001 << 4 = 0b10000 (16)
    12 >> 1,        // 0b01100 >> 1 = 0b00110 (6)
];
```

> Return value in JSON format

```json
[
    2,
    7,
    5,
    -6,
    16,
    6
]
```
