---
title: "type_info"
weight: 140
---

Returns information about a given [Type](../../data-types/type).

Value | Description
------- | -----------
`type_id` | Internal Type ID *(can be used to identify types in collection events)*.
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the type is created.
`modified_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the type is last modified or `nil` if never modified.
`name` | Type name.
`fields` | Array with arrays containing two strings, the property name and definition.

{{% notice note %}}
The `modified_at` time stamp is initially set to `nil` when the type is created using the [new_type(..)](../new_type) function.
It will be updated with a time stamp after modifying the type with either the [set_type(..)](../set_type) or the [mod_type(..)](../mod_type) function.
When the type is created with [set_type(..)](../set_type), then the `modified_at` property will be equal to `created_at`.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`type_info(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | str | The name of the Type for which the information about the properties has to be returned.


### Return value

Returns [info](../../data-types/info) about the type.

### Example

> This code shows the output of ***type_info()***:

```thingsdb,should_pass
// Just a type as an example
set_type('Book', {
    title: 'str',
    year: 'int',
});

// Return Type info
type_info('Book');
```

> Example return value in JSON format

```json
{
    "type_id": 0,
    "created_at": 1579175900,
    "modified_at": 1579175900,
    "name": "Book",
    "fields": [
        ["title", "str"],
        ["year", "int"]
    ]
}
```

