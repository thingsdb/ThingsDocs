---
title: "thing"
weight: 318
---

Returns a [thing](../../data-types/thing) from a specified value, that may be dynamic. If no value is given, a new thing is returned.

This function does *not* generate a [change](../../overview/changes).

### Function

`thing([id])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
id | int (optional) | The Id for the thing to return.

### Return value

Returns a [thing](../../data-types/thing).
A [lookup_err()](../../errors/lookup_err) is returned in case an Id is given which is not found inside the collection.

### Example

> This code shows an example usage of ***thing()***:

```thingsdb,should_pass
.greet = "Hello world!";
[
    thing(.id()),
    thing(),
];
```

> Example return value in JSON format

```json
[
    {
        "#": 42,
        "greet": "Hello world!"
    },
    {}
]
```
