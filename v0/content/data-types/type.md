---
title: "Type"
weight: 69
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

When using a list `'[]'` or set `'{}'` definition, it is also possible to make the list or set restricted to a certain type.
In this case only items of the given definition are allowed as members. For example `'[int]'` requires the members of a list
to be integers and `'{User}'` is a restricted set which only allows things of type *User*.


Both the list *and/or* the members can be made optional.
For example, this `'[str?]?'` is a valid declaration. Since a set does not allow for `nil` values, it is not possible to
make members of a `set` optional.

> This is an example using a restricted list:

```thingsdb,should_pass
// Very simple `Note` type
set_type('Note', {
    text: 'str',
    timestamp: 'uint'
});

// Book type with `notes` of type `Note`
set_type('Book', {
    title: 'str',
    notes: '[Note]'
});

// Create a new book
book = Book{
    title: "hitchhiker's guide to the galaxy",
    notes: []
};

// Add a note to the book
book.notes.push(Note{
    text: 'the answer is 42',
    timestamp: int(now())
});

// It *must* be a `Note`, something else is not allowed
assert(iserr(try(book.notes.push({test: 'not a Note'}))));

// Return the book, 2 levels deep to see the note
return(book, 2);
```

> Return value in JSON format

```json
{
    "notes": [
        {
            "text": "the answer is 42",
            "timestamp": 1573894579
        }
    ],
    "title": "hitchhiker's guide to the galaxy"
}
```
