---
title: "type_info"
weight: 180
---

Returns information about a given [Type](../../data-types/type).

Value | Description
------- | -----------
`type_id` | Internal Type ID *(can be used to identify Types in collection events)*.
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the Type is created.
`modified_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the Type is last modified or `nil` if never modified.
`name` | Type's name.
`fields` | Array with arrays containing two strings, the property name and definition.

{{% notice note %}}
The `modified_at` time stamp is initially set to `nil` when the Type is created using the [new_type(..)](../new_type) function.
It will be updated with a time stamp after modifying the Type with either the [set_type(..)](../set_type) or the [mod_type(..)](../mod_type) function.
When the Type is created with [set_type(..)](../set_type), then the `modified_at` property will be equal to `created_at`.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`type_info(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | The name of the Type for which the information about the properties has to be returned.

### Return value

Returns [info](../../data-types/info) about the Type.

### Example

> This code shows the output of ***type_info()***:

```thingsdb,should_pass
// Just a Type as an example
set_type('Book', {
    title: 'str',
    year: 'int',
    ratings: '[int]',
    get_rating: |this| {
        this.ratings
            ? this.ratings.reduce(|a, b| a+b, 0) / this.ratings.len()
            : nil;
    }
});

// Return Type info
type_info('Book');
```

> Example return value in JSON format

```json
{
    "created_at": 1593527321,
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
        ]
    ],
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
    "modified_at": null,
    "name": "Book",
    "type_id": 1
}
```
