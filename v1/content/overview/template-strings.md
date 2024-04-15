---
title: "Template Strings"
weight: 35
---

Template strings allows you to use embedded ThingsDB expressions to generate a string constant. Template strings are enclosed by the backtick (`) character instead of double or single quotes.

Here is an example of how they may be used:

```thingsdb,json_response
a = 6; b = 7;
`The sum of {a} plus {b} is {a + b}.`;
```
> Result in JSON format:

```json
"The sum of 6 plus 7 is 13."
```

If you wish to use the backtick character or curly brackets inside your string, then you need to escape those by using the same character twice. For example:

```thingsdb,json_response
`Example with ``Backticks`` and {{Curlies}}.`
```
> Result in JSON format:

```json
"Example with `Backticks` and {Curlies}."
```

