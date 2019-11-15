---
title: "thing"
date: 2019-10-14T10:05:54+02:00
weight: 3600
---

Returns a [thing](../../data-types/thing) from a specified value.
If no value is given, a new thing is returned.

This function does *not* generate an [event](../../events).

### Function

`thing([id])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
id | int (optional) | The id for the thing to return.

### Return value

Returns a [thing](../../data-types/thing).
An `INDEX_ERROR` is returned in case an id is given which is not found inside the collection.

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
