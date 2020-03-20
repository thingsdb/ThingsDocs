---
title: "Type"
weight: 94
---


A Type is like a thing with pre-defined properties.

### Definable properties

definition | description
---------- | -----------
`'str'` | requires type [str](../str) (values of type [str](../str) *should* contain valid UTF-8 characters).
`'utf8'` | requires type [str](../str) and the value *must* contain valid UTF-8 characters.
`'raw'` | requires type [str](../str) *or* [bytes](../bytes).
`'bytes'` | requires type [bytes](../bytes).
`'bool'` | requires type [bool](../bool).
`'int'` | requires type [int](../int).
`'uint'` | requires a *non-negative* integer (type [int](../int), `>= 0`).
`'pint'` | requires a *positive* integer (type [int](../int), `> 0`).
`'nint'` | requires a *negative* integer (type [int](../int), `< 0`).
`'float'` | requires type [float](../float).
`'number'` | requires type [float](../float) *or* type [int](../int).
`'thing'` | requires a [thing](../thing).
`'X'` | requires a instance of [Type](../type) `X`. The value `X` should be replace with the `Type` name.
`'[]'` | requires a [list](../list).
`'{}'` | requires a [set](../set).
`'any'` | any type is valid.

Each definition can be made optional by adding a question-mark `?` to the definition.
If a property is made optional, then the value `nil` is allowed instead of the given type.
The property will also be set to `nil` if no value for the property is given.

> For example

```thingsdb,json_response
// Create a new type `User` with an optional property `name`.
set_type('User', {name: 'str?'});

// Create a instance of type `User` without a name
unknown = User{};

// ..or explicitly set name to `nil`
user_nil = User{name: nil};

// ..a `str` is also ok
iris = User{name: 'Iris'};

// ..but another type than `str` or `nil` is not allowed
assert(iserr(try(User{name: 0})));

// Return the results
[unknown, user_nil, iris];
```

> Return value in JSON format

```json
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

### Related functions

Function | Description
------ | -----------
[del_type](../../collection-api/del_type) | Delete a `Type`.
[mod_type](../../collection-api/mod_type) | Modify an existing `Type` definition.
[new_type](../../collection-api/new_type) | Create a new `Type`.
[has_type](../../collection-api/has_type) | Determine if the current scope has a `Type`.
[set_type](../../collection-api/set_type) | Set property definitions on a `Type` and creates the `Type` if it did not exist.
[type_info](../../collection-api/type_info) | Return the `Type` definition.
[types_info](../../collection-api/types_info) | Return all `Type` definitions in the current scope.

### Mutation format

A mutation format is only required to understand if you manually want to parse events
when *watching* for mutations on *things*. While most values have a pretty straightforward
format when packed in a *mutation*, a Type instance is a bit more complex
to understand.

An example of a Type mutation:

```json
{
    ".": 10,
    "#": 123,
    "": [
        "hitchhiker's guide to the galaxy"
        4.2
    ]
}
```

Key | Description
--- | -----------
`"."` | The `type_id` of the Type.
`"#"` | The `#ID` which is assigned to the Type instance.
`""`  | Array with fields;

In order to correctly parse the mutation you require the [types_info](../../collection-api/types_info) of a collection.
Note that the types info is included inside an [init event](../../watching/on-init). Below is an example with an entry of `types_info`. This shows type **Book** which has ID `10` from the mutation example above.

```json
...
{
    "created_at": 1581454041,
    "fields": [
        ["title", "str"]
        ["rating", "float"]
    ],
    "modified_at": 1581455876,
    "name": "Book",
    "type_id": 10
}
...
```
