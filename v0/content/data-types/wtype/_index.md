---
title: "˂Type˃"
weight: 80
---


It is sometimes useful to get things with their ID (`#`) but still
be able to filter-out properties which are not required.

One feature to return only specific properties from a thing, is to work with *wrapped* types.
This feature is especially useful *(and fast)* if your source things are [Type](../type) instances.

In the [example](#example) below we show a use case for wrapping a book type. The set-up requires some code
but once the Types are defined, it is rather easy to use.


### Methods

Method | Description
------ | -----------
[unwrap](./unwrap) | Unwrap to access the *wrapped* thing..


### Example

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

// Create a Type to just return a writers `name`
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

// Create two sets `writers` and `books` to store all books and writers in
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
new_procedure('add_book', |author_name, book_title| wse({
    writer = .upsert_writer.call(author_name);
    new_book = Book{
        title: book_title,
        author: writer,
    };
    .books.add(new_book);
    writer.books.add(new_book);
}));

// Add some sample books
wse({
    run('add_book', 'Alice', 'Foo');
    run('add_book', 'Alice', 'Bar');
    run('add_book', 'Bob', 'Baz');
});

/*
 * Now we can simply wrap the collection to return the books with titles and
 * the author names including the thing ids.
 */
return(.wrap('_AllBooks'), 3);
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