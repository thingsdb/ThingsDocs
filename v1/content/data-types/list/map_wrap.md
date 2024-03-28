---
title: "map_wrap"
weight: 88
---

The function must be called on a list with *things* and returns a new list with every thing wrapped according the given type.

```thingsdb,syntax_only
// Take as example:
my_list.map_wrap('_SomeType');

// This is a fast shortcut for:
my_list.map(|item| item.wrap('_SomeType'));
```

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`map_wrap([Type])`

### Arguments

Argument | Arguments     | Description
-------- | ------------- | -----------
Type     | str (optional)| Type's name to wrap the thing with. If not given, the thing will be wrapped with its own type.

### Return value

A new list with the Ids for all the *things* in the original list.

### Example

> This code shows an example using ***map_wrap(..)***:

```thingsdb,json_response
set_type('_User', {name: 'str'});
users = [{name: "Iris", age: 9}, {name: "Sasha", age: 37}];

// returns a list with wrapped things
users.map_wrap('_User');
```

> Return value in JSON format

```json
[
    {
        "name": "Iris"
    },
    {
        "name": "Sasha"
    }
]
```
