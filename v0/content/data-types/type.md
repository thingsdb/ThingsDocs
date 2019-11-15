---
title: "Type"
date: 2019-10-23T16:43:16+02:00
weight: 1500
---


A Type is like a thing with pre-defined properties.


### Definable properties

definition | description
---------- | -----------
`'str'` | requires type [str](../str) and the value *should* contain valid UTF-8 characters.
`'utf8'` | requires type [str](../str) and the value is *must* be valid UTF-8.
`'raw'` | requires type [str](../str) *or* [bytes](../bytes).
`'bytes'` | requires type [bytes](../bytes).
`'int'` | requires type [int](../int).
`'uint'` | requires a *non-negative* type [int](../int).
`'thing'` | requires a [thing](../thing).
`'X'` | requires a instance of [Type](../type) `X`. The value `X` should be replace with the `Type` name.
`'[]'` | requires a [list](../list).
`'{}'` | requires a [set](../set).
`'any'` | any type is valid.


Each definition can be made optional by adding a question-mark `?` to the definition.
If a property is made optional, then the value `nil` is allowed instead of the give type.
The property will also be set to `nil` if no value for the property is given.

> For example

```
// Create a new type `User` with an optional property `name`.
set_type('User', {name: 'str?'});

// Create a instance of type `User` without a name
unknown = User{};

// ..or explicit set name to `nil`
user_nil = User{name: nil};

// ..a `str` is also ok
iris = User{name: 'Iris'};

// ..but another type than `str` or `nil` is not allowed
assert(iserr(try(User{name: 0})));

// Return the results
[unkown, user_nil, iris];
```

> Return value in JSON format

```
[
    {
        "name": null
    },
    {
        "name": null
    },
    {
        "name": "Iris"
    }
]
```

When using a list `'[]'` definition, it is also possible to allow only a certain type as members of the list.

> For example:

