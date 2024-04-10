---
title: "map_id"
weight: 125
---

The function returns a `list` with the Ids of all the things in the `set`.

```thingsdb,syntax_only
// Take as example:
my_set.map_id();

// This is a fast shortcut for:
my_set.map(|item| item.id());
```

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`map_id()`

### Arguments

None

### Return value

A list with the Ids for all the *things* in the original *set*.

### Example

> This code shows an example using ***map_id()***:

```thingsdb,should_pass
.users = set({name: "Iris", age: 9}, {name: "Sasha", age: 37});

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
