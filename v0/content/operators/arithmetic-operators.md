---
title: "Arithmetic operators"
weight: 145
---

Operator | Description
-------- | -----------
`+` | Addition operator.
`-` | Subtraction operator.
`/` | Division operator
`*` | Multiplication operator.
`%` | Modulo operator.

{{% notice tip %}}
Division uses float division if either the numerator or denominator is of type [float](../../data-types/float).
{{% /notice %}}

> Arithmetic examples:

```thingsdb,json_response
[
    5 + 2,
    5 - 2,
    5 / 2.0,
    5 / 2,
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
