---
title: "test"
date: 2019-10-14T10:05:45+02:00
weight: 55
---

Test if a string matches a given [regular expression](../../data-types/regex) and return `true` or `false`.

This function does *not* generate an [event](../../events).

### Function
*string*.`test(regex)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
regex | regex (required) | The regular expression to test against the string.

### Return value
`true` if there is a match between the string and the specified regular expression, otherwise `false`.

> Examples using ***test()***:

```
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
