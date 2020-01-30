---
title: "on-update"
weight: 189
---

An update event is pushed when a `thing` which you are watching, is updated.
If the thing contains other things, then these need to be watched separate to receive events when they are changed.

A not
```json
{
    "#": 3,
    "event": 123,
    "jobs": [
        ...
    ]
}
```

Job | Target | Description
--- | ------ | -----------
[splice](#splice) | `thing` |
[new_procedure](#new_procedure) | `collection` | A new procedure is added to the collection.


## splice

```thingsdb,syntax_only
// .arr = ["a", "b"];
.arr.push("c", "d");
```

```json
{
    "splice": {
        "arr": [2 , 0, "c", "d"]
    }
}
```


## new_procedure

```thingsdb,should_pass
new_procedure('multiply', |a, b| a*b);
```

```json
{
    "new_procedure": {
        "name": "multiply",
        "created_at": 1579601906,
        "closure": "|a,b|a*b"
    }
}
```
