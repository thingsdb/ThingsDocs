---
title: "Logical operators"
weight: 118
---

Logical operators are generally used with [bool](../../data-types/bool) values.

Operator | Description
-------- | -----------
`&&` | Logical AND.
`||` | Logical OR.

As logical expressions are evaluated left to right, they are tested for possible *"short-circuit"* evaluation. This means that the evaluation of an expression is stopped when the outcome is determined. This applies in the following two cases:

* `expression_1 && expression_2` : if `expression_1` evaluates to `false` then `expression_2` is not evaluated. Any side effects of doing so do not take place.

* `expression_1 || expression_2`: if `expression_1` evaluates to `true` then `expression_2` is not evaluated. Any side effects of doing so do not take place.

> Logical *short-circuit* examples:

```thingsdb,json_response
x = 0;
[
    false && x += 1,
    true || x += 1,
    x
];  // expression x += 1 will never be executed
```

> Return value in JSON format

```json
[
    false,
    true,
    0
]
```
