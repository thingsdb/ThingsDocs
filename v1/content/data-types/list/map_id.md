---
title: "map_id"
weight: 83
---

The function must be called on a list with *things* and returns a new list with the Ids of all the things.

```thingsdb,syntax_only
// Take as example:
my_list.map_id();

// This is a fast shortcut for:
my_list.map(|item| item.id());
```

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`map_id()`

### Arguments

None

### Return value

A new list with the Ids for all the *things* in the original list.

### Example

> This code shows an example using ***map_id()***:

```thingsdb,should_pass
.users = [{name: "Iris", age: 9}, {name: "Sasha", age: 37}];

// returns a list with Ids
.users.map_id();
```

> Example return value in JSON format

```json
[
    123,
    124
]
```
