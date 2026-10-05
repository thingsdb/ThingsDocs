---
title: "dict"
weight: 240
---

Returns a new [dict](../../data-types/dict) or converts an array of key-value pairs into a dict.

This function does *not* generate a [change](../../overview/changes).

### Function

`dict([value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | list (optional) | A list of key-value pairs to convert into a [dict](../../data-types/dict).

### Return value

A dict value.

{{% notice note %}}
In a client response, the dict is returned as an array of nested key-value pairs to preserve JSON compatibility when integer keys are used.
{{% /notice %}}

### Example

> This code shows how to create a dict:

```thingsdb,should_pass
dict([
    [uuid(), "Iris"],
    [uuid(), "Fleur"],
    [uuid(), "Fenna"],
    [uuid(), "Nissa"],
]);
```

> Example return value in JSON format _(order is not guaranteed)_

```json
[
  [
    "01a10c71-c2e4-79a5-8693-1503e026b8a8",
    "Iris"
  ],
  [
    "01a10c71-c2ea-7328-9c07-798440a1c4d8",
    "Nissa"
  ],
  [
    "01a10c71-c2ea-74fb-b226-4698a5e01e15",
    "Fenna"
  ],
  [
    "01a10c71-c2ea-760a-a61f-a3c593a870cd",
    "Fleur"
  ]
]
```
