---
title: "test"
weight: 85
---


Test if a [string](..) matches a given [regular expression](../../regex) and return `true` or `false`.

This function does *not* generate an [event](../../../overview/events).

### Function

*regex*.`test(string)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
string | str (required) | The string to test.

### Return value

`true` if there is a match between the string and the regular expression, otherwise `false`.

### Example

> Examples using ***test()***:

```thingsdb,json_response
// The first regex is case sensitive, the second is case insensitive
[
    regex("^hello").test('Hello world!!'),
    regex("^hello", "i").test('Hello world!!'),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
