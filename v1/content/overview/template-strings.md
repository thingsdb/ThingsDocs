---
title: "Template Strings"
weight: 38
---

Template strings allow you to use embedded ThingsDB expressions to generate a string value. Template strings are enclosed by the backtick (`` ` ``) character instead of double or single quotes.

Here is an example of how they may be used:

```thingsdb,json_response
a = 6; b = 7;
`The sum of {a} plus {b} is {a + b}.`;
```
> Return value in JSON format:

```json
"The sum of 6 plus 7 is 13."
```

If you wish to use the backtick character or curly brackets inside your string, then you need to escape those by using the same character twice. For example:

```thingsdb,json_response
`Example with ``Backticks`` and {{Curlies}}.`
```
> Return value in JSON format:

```json
"Example with `Backticks` and {Curlies}."
```

{{% notice note %}}
Template strings are evaluated immediately when executed. If you want to store a reusable template and render it later (or across different scopes), see the [template](../../data-types/template) data type.
{{% /notice %}}
