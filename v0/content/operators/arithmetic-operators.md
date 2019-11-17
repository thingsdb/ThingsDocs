---
title: "Arithmetic operators"
weight: 170
---

Operator | Description
-------- | -----------
`+` | Addition operator.
`-` | Subtraction operator.
`/` | Float division operator.
`//` | Integer division operator.
`*` | Multiplication operator.
`%` | Modulo operator.

> Arithmetic examples:

```thingsdb,json_response
[
    5 + 2,
    5 - 2,
    5 / 2,
    5 // 2,
    5 * 2,
    5 % 2,
];
```

> Return value in JSON format

```json
[
    7,
    3,
    2.5,
    2,
    10,
    1
]
```