---
title: "json_dump"
weight: 223
---

Converts a ThingsDB value in to a JSON [string](../../data-types/str).

This function does *not* generate a [change](../../overview/changes).

### Function

`json_dump(value, [options])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any | The value to convert into a JSON string.
options | thing | Thing with [options](#options).

### Options

Option | Type | Description
------ | ---- | -----------
deep | int | Specify how [deep](../../collection-api/return/#deep) the value must be converted. (defaults to `1`)
beautify | bool | Generate a JSON string with new lines and indentation to make the string more readable.

### Return value

JSON [string](../../data-types/str).

### Example

> This code shows an example for *json_dump*:

```thingsdb,json_response
json_dump({
    success: true
});
```

> Return value in JSON format

```json
"{\"success\":true}"
```

> Another example with extra options:

```thingsdb,json_response
data = {
    people: [
        {name: 'Iris'},
        {name: 'Tess'},
    ]
};
json_dump(data, {deep: 2});
```

> Return value in JSON format

```json
"{\"people\":[{\"name\":\"Iris\"},{\"name\":\"Tess\"}]}"
```