---
title: "Type"
weight: 138
---


A Type is like a thing with pre-defined properties and/or methods. When an instance of a Type is created,
all defined properties are guaranteed to exist with a value matching the Type definition.


### Definable properties

definition | default | description
---------- | ------- | -----------
`'str'` | `""` | requires type [str](../str) (values of type [str](../str) *should* contain valid UTF-8 characters).
`'str<..>'` | *depends* | requires type [str](../str) with a certain length *(see [length condition](#length-condition) and [default value](#use-condition-to-set-a-default-value))*
`/pattern/` | *depends* | requires type [str](../str) with a math to a specified pattern *(see [pattern condition](#pattern-condition))*.
`'utf8'` | `""` | requires type [str](../str) and the value *must* contain valid UTF-8 characters.
`'raw'` | `""` | requires type [str](../str) *or* [bytes](../bytes).
`'bytes'` | `bytes()` | requires type [bytes](../bytes).
`'bool'` | `false` | requires type [bool](../bool).
`'int'` | `0` | requires type [int](../int).
`'int<..>'` | *depends* | requires type [int](../int) within a given range *(see [range condition](#range-condition)  and [default value](#use-condition-to-set-a-default-value))*.
`'uint'` | `0` | requires a *non-negative* integer (type [int](../int), `>= 0`).
`'pint'` | `1` | requires a *positive* integer (type [int](../int), `> 0`).
`'nint'` | `-1` | requires a *negative* integer (type [int](../int), `< 0`).
`'float'` | `0.0` | requires type [float](../float).
`'float<..>'` | *depends* | requires type [float](../float) within a given range *(see [range condition](#range-condition) and [default value](#use-condition-to-set-a-default-value))*.
`'number'` | `0` | requires type [float](../float) *or* type [int](../int).
`'datetime'` | `datetime()` | requires type [datetime](../datetime). *(defaults to the current date/time)*
`'timeval'` | `timeval()` | requires type [timeval](../timeval). *(defaults to the current date/time)*
`'thing'` | `{}` | requires a [thing](../thing).
`'X'` | `X{}` | requires a instance of [Type](../type) `X`, or a member of [enumerator](../enum) `X`. The value `X` should be replaced with the `Type` / `enum` name.
`'[]'` | `[]` | requires a [list](../list).
`'{}'` | `set()` | requires a [set](../set).
`'any'` | `nil` | any type is valid.

Each definition can be made optional by adding a question-mark `?` to the definition.
If a property is made optional, then the value `nil` is allowed instead of the given type
and `nil` will also be the default if the property is missing.

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
assert(is_err(try(User{name: 0})));

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
};

// Add a note to the book
book.notes.push(Note{
    text: 'the answer is 42',
    timestamp: int(now())
});

// It *must* be a `Note`, something else is not allowed
assert(is_err(try(book.notes.push({test: 'not a Note'}))));

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

### Length condition

A length condition may be added to a `str` type definition using the following syntax:

```
str<min:max:default>
```

argument  | description
--------  | -----------
`min`     | Optional minimal length *(inclusive)*.
`max`     | Optional maximum length *(inclusive, this value must be equal to or greater than `min`)*.
`default` | Optional default value. If not given, the default value will be the smallest possible string filled with the dash (`-`) character.

For example:

```thingsdb,json_response
set_type('Person', {
    name: 'str<1:10>',
    email: 'str<3:50:info@thingsdb.net>'
});

/*
 *  Each Person instance will contain a name with at least 1 character
 *  and at most 10 characters and an email property with a string of at
 *  least 3 and at most 50 characters.
 */

Person{};  // return a Person with default values
```

> Return value in JSON format

```json
{
    "name": "-",
    "email": "info@thingsdb.net"
}
```

{{% notice warning %}}
It is not possible to use a length condition as a nested array definition. For example, something like `"[str<1:10>]"` is ***not*** allowed.
{{% /notice %}}

### Pattern condition

A pattern condition applies to type `str` and may be used using the following syntax:

```text
/pattern/i
```

The `i` is optional and tells the pattern to be case insensitive. If left away, the pattern will thus be case sensitive.

The definition must be either *nillable* by adding a `?` to the definition or an empty string must match with the given pattern. If this is *not* the case, then a default value ***must*** be given using the syntax below:

```text
/pattern/i<default>
```

{{% notice note %}}
It is always possible to set a default value as long as the default value matches
with the given pattern.
{{% /notice %}}

Here is an example using some pattern conditions:

```thingsdb,json_response
set_type('Words', {
    example1: '/^(e|h|l|o)*$/',
    example2: '/thingsdb/i<ThingsDB>',
    example3: '/^[0-9]{4}[A-Z]{2}$/?',
    example4: '/^[0-9]{4}[A-Z]{2}$/<1234AB>?',
});

/*
 *  example1 - matches an empty string so a default value is not required
 *  example2 - case insensitive and requires a default value
 *  example3 - nillable and thus no default value is required
 *  example4 - exactly the same as example3 but with a default value
 */

Words{};  // return a Person with default values
```

> Return value in JSON format

```json
{
    "example1": "",
    "example2": "ThingsDB",
    "example3": null,
    "example4": "1234AB"
}
```

{{% notice warning %}}
A pattern condition cannot be used as a nested array definition, thus something like `"[/pattern/i]"` is ***not*** possible.
{{% /notice %}}

### Range condition

A range condition may be added to a `int` or `float` type definition using the following syntax:

```
int<min:max:default>
```

Or

```
float<min:max:default>
```

argument  | description
--------  | -----------
`min`     | Optional minimal value *(inclusive)*.
`max`     | Optional maximum value *(inclusive, this value must be equal to or greater than `min`)*.
`default` | Optional default value. If not given, the default value will be the closest possible value towards zero (`0`).

For example:

```thingsdb,json_response
set_type('Values', {
    a: 'int<10:20>',
    b: 'int<0:10:5>',
    c: 'float<-1:1>',
    d: 'float<0:1:0.5>',
});


Values{};  // return a `Values` instance with default values
```

> Return value in JSON format

```json
{
    "a": 10,
    "b": 5,
    "c": 0,
    "d": 0.5
}
```

{{% notice warning %}}
A range condition cannot be used as a nested array definition, thus something like `"[int<1:10>]"` is ***not*** possible.
{{% /notice %}}

### Use condition to set a default value

Both the `min` and `max` of a *range* and *length* condition are optional. For this reason you can use the *"condition"* syntax to configure a default value for a property on a Type.

*(You may want to combine a default value with a minimum and/or maximum limit and that is fine; This example is just to make it clear that setting a `min` and/or `max` value is not required.)*

For example:

```thingsdb,json_response
set_type('TestDefault', {
    f: 'float<::3.14>',
    i: 'int<::42>',
    s: 'str<::ThingsDB>',
});

TestDefault{};  // return a `TestDefault` instance with default values
```

> Return value in JSON format

```json
{
    "f": 3.14,
    "i": 42,
    "s": "ThingsDB"
}
```

### Get instance of a type

The [thing(..)](../../collection-api/thing) function may be used to get an instance
of a given Id. This does not guarantee that the *thing* is truly of the type you expect.
Instead of adding a [type_assert(..)](../../collection-api/type_assert) on the *thing*, it is also possible to
call the type as a function with the Id as it's first argument.

For example:

```thingsdb,syntax_only
// Suppose we have a user_id and want to get the user
user = User(user_id);
```

Possible errors:

- A [lookup_err()](../../errors/lookup_err) will be raised if no *thing* with the given `user_id` exists.
- A [type_err()](../../errors/type_err) will be raised if a *thing* is found, but the *thing* is not of the *User* type,

### Methods

A method is a closure attached to a type. Methods are defined when creating a type by attaching a closure instead of a [definition](#definable-properties).
When a method is used on an instance of a type, the first argument will be the *instance* itself. It is therefore common to name the first argument `this`.

For example:

```thingsdb,json_response
set_type('Person', {
    name: 'str',
    age: 'int',
    whoami: |this| `My name is {this.name} and I am {this.age} years old.`
});

.iris = Person{
    name: 'Iris',
    age: 7
};

.iris.whoami();
```

> Return value in JSON format

```json
"My name is Iris and I am 7 years old."
```


### Related functions

Function | Description
------ | -----------
[del_type](../../collection-api/del_type) | Delete a `Type`.
[has_type](../../collection-api/has_type) | Determine if the current scope has a `Type`.
[mod_type](../../collection-api/mod_type) | Modify an existing `Type` definition.
[new_type](../../collection-api/new_type) | Create a new `Type`.
[rename_type](../../collection-api/rename_type) | Rename the `Type`.
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
Note that the types info is included inside an [init event](../../watching/on-init). Below is an example with an entry of `types_info`. This shows type **Book** which has Id `10` from the mutation example above.

```json
...
{
    "created_at": 1581454041,
    "fields": [
        ["title", "str"]
        ["rating", "float"]
    ],
    "methods": {},
    "modified_at": 1581455876,
    "name": "Book",
    "type_id": 10,
    "wrap_only": false
}
...
```
