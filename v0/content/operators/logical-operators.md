---
title: "Logical operators"
weight: 84
---

Logical operators are typically used with [bool](../../data-types/bool) values.

Operator | Description
-------- | -----------
`&&` | Logical AND.
<code>&#124;&#124;</code> | Logical OR.

As logical expressions are evaluated left to right, they are tested for possible *"short-circuit"* evaluation using the following rules:

- `(some falsy expression) && expr` is short-circuit evaluated to the falsy expression;
- `(some truthy expression) || expr` is short-circuit evaluated to the truthy expression.

Short circuit means that the `expr` parts above are not evaluated, hence any side effects of doing so do not take effect
(e.g., if expr is a function call, the calling never takes place).
This happens because the value of the operator is already determined after the evaluation of the first operand.

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
