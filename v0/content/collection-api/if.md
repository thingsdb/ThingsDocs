---
title: "if"
weight: 158
---

Runs a block code based on the result of a given condition.

{{% notice note %}}
ThingsDB uses *lazy-evaluation* of function arguments. For this reason *if()* is a function call, and not a statement like in most other languages.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`if(condition, if_true, [if_false])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`condition` | any (required) | The condition to evaluate.
`if_true` | any (required) | Will be executed when the condition evaluated to `true`.
`if_false` | any (optional) | Will be executed when the condition evaluated to `false`.

### Return value

Returns `nil`.

### Example

> This code shows how *if(..)* can be used:

```thingsdb,json_response
if(2 > 1, {
    return("two is more than one");
});

"math is broken";
```

> Return value in JSON format

```json
"two is more than one"
```
