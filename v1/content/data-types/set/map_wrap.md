---
title: "map_wrap"
weight: 126
---

The function returns a `list` with every thing wrapped according the given type.

```thingsdb,syntax_only
// Take as example:
my_set.map_wrap('_SomeType');

// This is a fast shortcut for:
my_set.map(|item| item.wrap('_SomeType'));
```

This function does *not* generate a [change](../../../overview/changes).

### Function

*set*.`map_wrap([Type])`

### Arguments

Argument | Arguments     | Description
-------- | ------------- | -----------
Type     | str (optional)| Type's name to wrap the thing with. If not given, the thing will be wrapped with its own type.

### Return value

A `list` with the Ids for all the *things* in the original *set*.

### Example

> This code shows an example using ***map_wrap(..)***:

```thingsdb,json_response
set_type('_User', {name: 'str'});
users = [{name: "Iris", age: 9}];

// returns a list with wrapped things
users.map_wrap('_User');
```

> Return value in JSON format

```json
[
    {
        "name": "Iris"
    }
]
```
