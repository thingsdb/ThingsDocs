---
title: "type_info"
weight: 296
---

Returns information about a given [Type](../../overview/type).

Value | Description
------- | -----------
`type_id` | Internal Type Id.
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the Type is created.
`modified_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the Type is last modified or `nil` if never modified.
`name` | Type's name.
`fields` | Array with arrays containing two strings, the property name and definition.
`methods` | Object with methods where the key is the method name and the value an object containing information about the closure.
`relations` | Object with [relations](../mod_type/rel).
`hide_id` | Boolean indication if this type has *hide_id_* enabled or not.
`wrap_only` | Boolean indication if this type has *wrap-only* mode enabled or not.

{{% notice info %}}
Methods information will contain the definition of the attached closure ***only*** when the user has at least `CHANGE` privileges on the collection containing the type.
{{% /notice %}}

{{% notice note %}}
The `modified_at` time stamp is initially set to `nil` when the Type is created using the [new_type(..)](../new_type) function.
It will be updated with a time stamp after modifying the Type with either the [set_type(..)](../set_type) or the [mod_type(..)](../mod_type) function.
When the Type is created with [set_type(..)](../set_type), then the `modified_at` property will be equal to `created_at`.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`type_info(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | The name of the Type for which the information about the properties has to be returned.

### Return value

Returns [mpdata](../../data-types/mpdata) about the Type.

### Example

> This code shows the output of ***type_info()***:

```thingsdb,should_pass
new_type('Book');

// Just a Type as an example
set_type('Book', {
    title: 'str',
    year: 'int',
    ratings: '[int]',
    get_rating: |this| {
        this.ratings
            ? this.ratings.reduce(|a, b| a+b, 0) / this.ratings.len()
            : nil;
    },
    similar: '{Book}'
});

// Create a relation on Book.similar
// If a book is similar to a book, it is most likely also true the other
// way around.
mod_type('Book', 'rel', 'similar', 'similar');

// Return Type info
type_info('Book');
```

> Example return value in JSON format

```json
{
    "created_at": 1613736754,
    "fields": [
        [
            "title",
            "str"
        ],
        [
            "year",
            "int"
        ],
        [
            "ratings",
            "[int]"
        ],
        [
            "similar",
            "{Book}"
        ]
    ],
    "hide_id": false,
    "methods": {
        "get_rating": {
            "arguments": [
                "this"
            ],
            "definition": "|this| {\n    this.ratings\n        ? this.ratings.reduce(|a, b| a + b, 0) / this.ratings.len()\n        : nil;\n}",
            "doc": "",
            "with_side_effects": false
        }
    },
    "modified_at": 1613736754,
    "name": "Book",
    "relations": {
        "similar": {
            "definition": "{Book}",
            "property": "similar",
            "type": "Book"
        }
    },
    "type_id": 0,
    "wrap_only": false
}
```
