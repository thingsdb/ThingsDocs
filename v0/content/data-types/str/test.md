---
title: "test"
weight: 106
---

{{% notice warning %}}
This function is deprecated and should be replaced with [test(..)](../../../data-types/regex/test) on type [regex](../../../data-types/regex).
{{% /notice %}}

Test if a [string](..) matches a given [regular expression](../../regex) and return `true` or `false`.

This function does *not* generate an [event](../../../overview/events).

### Function

*str*.`test(regex)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
regex | regex (required) | The regular expression to test against the string.

### Return value

`true` if there is a match between the string and the specified regular expression, otherwise `false`.

### Example

> Examples using ***test()***:

```thingsdb,json_response
[
    'Hello world!!'.test(/^hello/),
    'Hello world!!'.test(/^hello/i),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
