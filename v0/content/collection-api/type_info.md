---
title: "type_info"
weight: 138
---

Returns information about a given [Type](../../data-types/type).

Value | Description
------- | -----------
type_id | Internal Type ID *(can be used to identify types in collection events)*.
name | Type name.
fields | Array with arrays containing two strings, the property name and definition.

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

```thingsdb,json_response
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
    "name": "Book",
    "fields": [
        ["title", "str"],
        ["year", "int"]
    ]
}
```

