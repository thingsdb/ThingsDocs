---
title: "Type"
weight: 38
---


Use a Type to create [typed](../../data-types/typed) things.

A *[typed](../../data-types/typed)* thing is a thing with predefined properties and/or methods with are defined by a *Type*.
When creating a *[typed](../../data-types/typed)* thing, all defined properties of the *type* are guaranteed to exist with a value matching the type definition.


### Definable properties

definition | default | description
---------- | ------- | -----------
`'str'` | `""` | requires type [str](../../data-types/str) (values of type [str](../../data-types/str) *should* contain valid UTF-8 characters).
`'str<..>'` | *depends* | requires type [str](../../data-types/str) with a certain length *(see [length condition](#length-condition) and [default value](#use-condition-to-set-a-default-value))*
`'/pattern/'` | *depends* | requires type [str](../../data-types/str) with a match to a specified pattern *(see [pattern condition](#pattern-condition))*.
`'utf8'` | `""` | requires type [str](../../data-types/str) and the value *must* contain valid UTF-8 characters.
`'utf8<..>'` | *depends* | requires type [str](../../data-types/str), the value *must* contain valid UTF-8 characters and with a certain length *(see [length condition](#length-condition) and [default value](#use-condition-to-set-a-default-value))*
`'raw'` | `""` | requires type [str](../../data-types/str) *or* [bytes](../../data-types/bytes).
`'bytes'` | `bytes()` | requires type [bytes](../../data-types/bytes).
`'bool'` | `false` | requires type [bool](../../data-types/bool).
`'bool<..>'` | *depends* | like `bool` but with an custom default, for example: `bool<true>`.
`'int'` | `0` | requires type [int](../../data-types/int).
`'int<..>'` | *depends* | requires type [int](../../data-types/int) within a given range *(see [range condition](#range-condition) and [default value](#use-condition-to-set-a-default-value))*.
`'uint'` | `0` | requires a *non-negative* integer (type [int](../../data-types/int), `>= 0`).
`'pint'` | `1` | requires a *positive* integer (type [int](../../data-types/int), `> 0`).
`'nint'` | `-1` | requires a *negative* integer (type [int](../../data-types/int), `< 0`).
`'float'` | `0.0` | requires type [float](../../data-types/float).
`'float<..>'` | *depends* | requires type [float](../../data-types/float) within a given range *(see [range condition](#range-condition) and [default value](#use-condition-to-set-a-default-value))*.
`'number'` | `0` | requires type [float](../../data-types/float) *or* type [int](../../data-types/int).
`'datetime'` | `datetime()` | requires type [datetime](../../data-types/datetime). *(defaults to the current date/time)*
`'timeval'` | `timeval()` | requires type [timeval](../../data-types/timeval). *(defaults to the current date/time)*
`'regex'` | `regex('.*')` | requires type [regex](../../data-types/regex).
`'closure'` | `\|\|nil` | requires type [closure](../../data-types/closure).
`'error'` | `err()` | requires type [error](../../data-types/error).
`'room'` | `room()` | requires type [room](../../data-types/room).
`'task'` | `task()` | requires type [task](../../data-types/task).
`'thing'` | `{}` | requires a [thing](../../data-types/thing).
`'thing<T>'` | `{}` | requires a value restricted [thing](../../data-types/thing) where each value must be of type `T`.
`'T'` | `T{}` | requires a instance of [Type](../type) `T`, or a member of [enumerator](../../data-types/enum) `T`. The value `T` should be replaced with the `Type` / `enum` name.
`'E{M}'` | `E{M}` | requires a instance of a member of [enumerator](../../data-types/enum). Instead of the enumerator default, member `M` will be used as the default value.
`'email'` | `""` | requires type [str](../../data-types/str) and the value *must* contain an email address _(or empty string)_.
`'email<..>'` | *depends* | requires type [str](../../data-types/str) and the value *must* contain an email address _(empty string is not allowed, a [default email address](#use-condition-to-set-a-default-value) must be given)_.
`'url'` | `""` | requires type [str](../../data-types/str) and the value *must* contain a URL _(or empty string)_.
`'url<..>'` | *depends* | requires type [str](../../data-types/str) and the value *must* contain a URL _(empty string is not allowed and a [default URL](#use-condition-to-set-a-default-value) must be given)_.
`'tel'` | `""` | requires type [str](../../data-types/str) and the value *must* contain a telephone number _(or empty string)_.
`'tel<..>'` | *depends* | requires type [str](../../data-types/str) and the value *must* contain a telephone number _(empty string is not allowed, a [default telephone number](#use-condition-to-set-a-default-value) must be given)_.
`'[]'` | `[]` | requires a [list](../../data-types/list).
`'[T]'` | `[]` | requires a [list](../../data-types/list) where each item in the list must be of type `T` *(see [restrict items](#restrict-items))*.
`'{}'` | `set()` | requires a [set](../../data-types/set).
`'{T}'` | `set()` | requires a [set](../../data-types/set) where each element in the set must be of type `T` *(see [restrict items](#restrict-items))*.
`'any'` | `nil` | any type is valid *(with the exception of a [future](../../data-types/future))*.
`'#'` | *depends* | Not a real property, see [named Id](#named-id).

Each definition can be made optional by adding a question-mark `?` to the definition and can be prefixed with additional [wrap flags](#wrap-prefix-flags).
If a property is made optional, then the value `nil` is allowed instead of the given type
and `nil` will also be the default if the property is missing.

> For example

```thingsdb,json_response
// Create a new type `User` with an optional property `name`.
set_type('User', {name: 'str?'});

// Create a typed thing of type `User` without a name
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
### Wrap (Prefix) flags

All definitions can be pre-fixed with additional flags which are applied when a thing is being wrapped.

Flag | Description
---- | -----------
`&`  | Tell ThingsDB to use the same *deep* level as the parent. See [documentation](#same-deep-level) below for more information.
`+`  | Fakes the parent to have a deep level of `127` and therefore this property will get a deep level of `126`. _(Not possible in combination with the `-` flag)_
`-`  | Fakes the parent to have a deep level of `1` and therefore this property will get a deep level of `0`. Note: both the `&` and `-` flags combination enforces a deep level of exactly `1`.
`^`  | Tell ThingsDB to use the `NO_IDS` return flag on this property. See [return flags](../statements#return-flags) for more information.
`*`  | When the value is a member of an enumerator, return the _name_ instead of the _value_.
`?`  | Exclude the property when the value is `nil`.

### Same deep level

Any definable property can be pre-fixed with a `&` character which is only used after the type is used to wrap and tells to use the same *deep* level for this property.
Although the character is allowed everywhere, it only has effect when the value is or contains *thing(s)*. Only a *thing* honors *deep* thus this makes sense.

> For example

```thingsdb,json_response
new_type('User');
set_type('User', {
    name: 'str',
    friend: '&User?'
});

iris = User{
    name: 'Iris',
    friend: User{
        name: 'Cato'
    }
};

iris.wrap();
```

> Return value in JSON format

```json
{
    "friend": {
        "friend": null,
        "name": "Cato"
    },
    "name": "Iris"
}
```

### Named Id

ThingsDB returns the Id of a thing as property `#`. Thus, as an example you might get a result like this:

```thingsdb,should_pass
set_type('Person', {name: 'str'});
.alice = Person{name: 'Alice'};
```

> Returns with something like:
```json
{
    "#": 123,
    "name": "Alice"
}
```

If we want something else than `#`, what we can do is define some property, for example `id` with the `#` definition:

```thingsdb,should_pass
set_type('Person', {id: '#', name: 'str'});
.alice = Person{name: 'Alice'};
```

> Returns with something like:
```json
{
    "id": 123,
    "name": "Alice"
}
```

### Restrict items

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
return book, 2;
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

A length condition may be added to a `str` or `utf8` type definition using the following syntax:

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
    email: 'str<3:50:info@thingsdb.io>'
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
    "email": "info@thingsdb.io"
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

For `email`, `url` and `tel`, you can also set a default value, for example:

```thingsdb,json_response
set_type('TestDefault', {
    e: 'email<info@thingsdb.io>',
    u: 'url<https://thingsdb.io>',
    t: 'tel<(0031) 6 1279 8880>',
});

TestDefault{};  // return a `TestDefault` instance with default values
```

> Return value in JSON format

```json
{
    "e": "info@thingsdb.io",
    "t": "(0031) 6 1279 8880",
    "u": "https://thingsdb.io"
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
