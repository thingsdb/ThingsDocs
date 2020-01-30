---
title: "Precedence and associativity"
weight: 89
---

Symbol | Type of operation | Associativity
------ | ----------------- | -------------
`()`   | Expression parenthesis | Left-to-right
`!`    | Not operator | Right-to-left
`*` `/` `//` `%` | Multiplication, Modulo, (Integer) Division | Left-to-right
`+` `-` | Add, Subtract | Left-to-right
`&` | Bitwise AND | Left-to-right
`^` | Bitwise XOR | Left-to-right
<code>&#124;</code> | Bitwise OR | Left-to-right
`==` `!=` `<=` `>=` `<` `>` | Compare | Left-to-right
`&&` | Logical AND | Left-to-right
<code>&#124;&#124;</code> | Logical OR | Left-to-right
`? :` | Conditional | Right-to-left
`=` `*=` `/=` `%=` `+=` `-=` `&=` `^=` <code>&#124;=</code> | Assignments | Right-to-left
