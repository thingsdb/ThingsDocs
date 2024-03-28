---
title: "map_type"
weight: 87
---

The function must be called on a list with *Ids (integer values)* or *things* and returns a new list with the Ids and things converted to corresponding [typed](../../typed) things.

```thingsdb,syntax_only
// Take as example:
my_list.map_type('MyType');

// This is a fast shortcut for:
my_list.map(|item| MyType(item));
```

This function does *not* generate a [change](../../../overview/changes).

### Function

*array*.`map_type(Type)`

### Arguments

Argument | Arguments   | Description
-------- | ----------- | -----------
Type     | str         | Convert the items in the list to this Type.

### Return value

A new list with each item of the original list converted to a typed *thing* of the given Type.

### Example

> This code shows an example using ***map_type(..)***:

```thingsdb,json_response
set_type('User', {name: 'str', age: 'int'});
users = [{name: "Iris", age: 9}, {name: "Sasha", age: 37}];

// returns a list with things of type User
users = users.map_type('User');

// every item is of type User
assert( users.every(|item| type(item) == 'User') );

// return the list of users
users
```

> Return value in JSON format

```json
[
    {
        "name": "Iris",
        "age": 9
    },
    {
        "name": "Sasha",
        "age": 37
    }
]
```
