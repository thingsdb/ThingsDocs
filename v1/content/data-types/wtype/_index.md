---
title: "˂Type˃"
weight: 188
---


It is sometimes useful to get things with their Id (`#`) but still
be able to filter-out properties which are not required.

A solution to return only specific properties from a thing, is to work with *wrapped* Types.
This feature is especially useful *(and fast)* if your source thing is a [typed](../typed) thing.

Besides filtering properties, a wrapped *thing* also inherits the [methods](../type/#methods) from the *type* it is wrapped with *(see [example 3](#example-3))*. When a wrapped type is returned to the client,
those methods act as [computed properties](#computed-properties). *(see [example 4](#example-4), [example 5](#example-5) and [example 6](#example-6))*


{{% notice note %}}

When ThingsDB wraps a thing with a Type, each property must be compared to the definition of that Type to determine if it comes in the end result. However, if the source is *typed* thing, ThingsDB only needs to do this once and can use an internal cache for every other transition from that Type to Type.

{{% /notice %}}

In the [example](#example-1) below we show a use case for wrapping a book type. The set-up requires some code
but once the Types are defined, it is rather easy to use.

### Functions

Function | Description
------ | -----------
[copy](./copy) | Copy the *wrapped* thing to a new thing.
[dup](./dup) | Duplicate the *wrapped* thing *as-is* and keep the wrap.
[unwrap](./unwrap) | Unwrap to access the *wrapped* thing..

### Example 1

```thingsdb,should_pass
new_type('Writer');

// Create type `Book`
set_type('Book', {
    title: 'str',
    author: 'Writer'
});

// Create type `Writer`
set_type('Writer', {
    name: 'str',
    books: '{Book}',
});

// Create a Type to just return a writer's `name`
set_type('_WriterName', {
    name: 'any'
});

// Create a Type for returning a `title` and author as `_WriterName`
set_type('_Book', {
    title: 'any',
    author: '_WriterName'
});

// Create a Type for returning only a set of `books` as `_Book`
set_type('_AllBooks', {
    books: '{_Book}'
});

// Create two sets, `writers` and `books`, to store all books and writers in
.writers = set();
.books = set();

// A closure function to return a writer by name and create if not exists
.upsert_writer = |name| {
    "Return the writer if exists, or create a new one";
    .writers.find(|w| w.name == author_name) || {
        new_writer = Writer{
            name: author_name,
            books: set()
        };
        .writers.add(new_writer);
        new_writer;
    };
};

// Create a procedure for adding a new book
new_procedure('add_book', |author_name, book_title| {
    writer = .upsert_writer(author_name);
    new_book = Book{
        title: book_title,
        author: writer,
    };
    .books.add(new_book);
    writer.books.add(new_book);
});

// Add some sample books
run('add_book', 'Alice', 'Foo');
run('add_book', 'Alice', 'Bar');
run('add_book', 'Bob', 'Baz');

/*
 * Now we can simply wrap the collection to return the books with titles and
 * the author names including the thing-ids.
 */
return .wrap('_AllBooks'), 3;
```

```json
{
    "#": 4,
    "books": [
        {
            "#": 6,
            "author": {
                "#": 5,
                "name": "Alice"
            },
            "title": "Foo"
        },
        {
            "#": 7,
            "author": {
                "#": 5,
                "name": "Alice"
            },
            "title": "Bar"
        },
        {
            "#": 9,
            "author": {
                "#": 8,
                "name": "Bob"
            },
            "title": "Baz"
        }
    ]
}
```

### What if a Type is removed?

When a Type is removed that was wrapping things, all these things are not filtered anymore. However these things are still connected to the removed Type's name. In case you decide to add a Type with the same name, then the wrapped things will be filtered again according to the Type's new definition. The following [example](#example-2) will demonstrate this event.

### Example 2

```thingsdb,should_pass
// Create type `Person`
set_type('Person', {
    firstName: 'str',
    lastName: 'str',
    age: 'int',
    gender: 'str',
});

// Create type `PersonName`, only includes the names of the person.
set_type('PersonName', {
    firstName: 'str',
    lastName: 'str',
});

// Create a thing with type `Person`
.Bob = Person{
    firstName: 'Bob',
    lastName: 'Lightyear',
    age: 43,
    gender: 'male',
};

// Wrap .Bob and store the wrapped thing.
.WrappedBob = .Bob.wrap('PersonName');

// Return the wrapped type
.WrappedBob;
```

The output:

```json
{
    "#": 21,
    "firstName": "Bob",
    "lastName": "Lightyear"
}
```

But now the type `PersonName`will be deleted.

```thingsdb,syntax_only
// Delete type `PersonName`. After deleting this Type `.WrappedBob` is not filtered
del_type('PersonName');

// ...but returns all properties stored.
.WrappedBob;
```

The output of the property `.WrappedBob` is not filtered, but in fact returns all its containing properties.

```json
{
    "#": 21,
    "age": 43,
    "firstName": "Bob",
    "gender": "male",
    "lastName": "Lightyear"
}
```

If we subsequently add a type called `PersonName`again (with in this case a different set of properties), then the output to querying `.WrappedBob` is filtered by the type `PersonName` again.

```thingsdb,syntax_only
// Create the type `PersonName` again, but with a different set of properties.
set_type('PersonName', {
    lastName: 'str',
});

// And return `.WrappedBob` again.
.WrappedBob;
```

The output now only includes the `lastName` property. Thus the property `.WrappedBob` did not loose its wrapping with type `PersonName` after it got deleted.

```json
{
    "#": 21,
    "lastName": "Lightyear"
}
```

### Example 3

> This last example show how methods of a type are inherited by a wrapped type:

```thingsdb,json_response
set_type('MathXY', {
    multiply: |this| this.x * this.y,
    add: |this| this.x + this.y,
});

set_type('Point2d', {
    x: 'number',
    y: 'number',
});

point = Point2d{
    x: 6,
    y: 7,
};

point.wrap('MathXY').multiply();
```

> Return value in JSON format:

```json
42
```

### Computed properties

Sometimes you want to wrap a type and compute some additional properties.
A good example might be the count for some messages.

### Example 4

```thingsdb,json_response
set_type('Person', {
    name: 'str',
    messages: '[str]',
});

// Now we want to return a person but only need the number of message,
// not the actual messages...

// Create a `wrap-only` type and specify the name and an additional `mcount` method
set_type('_Pmcount', {
    name: 'any',
    mcount: |p| p.messages.len()
}, true);

// If we now, with the above in place, create a person and wrap the person with _Pmcount:
p = Person{
    name: 'iris',
    messages: ['hi', 'hello', 'bye']
};
p.wrap('_Pmcount');
```

> Return value in JSON format

```json
{
            "name": "iris",
            "mcount": 3
}
```

### Example 5

It is also possible to overwrite the same property name, for example:

```thingsdb,json_response
set_type('Person', {
    name: 'str',
    messages: '[str]',
});

// Overwriting properties is possible
set_type('_Poverwrite', {
    name: |p| p.name.upper(),
    messages: |p| p.messages.len(),
}, true);

p = Person{
    name: 'iris',
    messages: ['hi', 'hello', 'bye']
};
p.wrap('_Poverwrite');
```

> The code above Will give the following result in JSON format

```json
{
            "name": "IRIS",
            "messages": 3
}
```

### Example 6

Computed properties may also have their own *depth* which does not affect the other properties

```
set_type('Foo', {
    bar: 'thing',
});

set_type('_Pexample', {
    bar: 'any',
    other: || return {a: {b: 5}}, 2
}, true);

foo = Foo{
    bar: {x: {y: 6}},
};
foo.wrap(_Pexample); // Return one deep, note that `other` has it's own depth
```

> Return value in JSON format

```json
{
            "bar": {},
            "other": {"x": {"y": 6}}
}

```
