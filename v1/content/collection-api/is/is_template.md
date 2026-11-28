---
title: "is_regex"
weight: 291
---

This function determines whether the provided value is of type [template](../../../data-types/template) or not.

This function does *not* generate a [change](../../../overview/changes).

### Function

`is_template(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is of type [template](../../../data-types/template), else it returns `false`.

### Example

> This code shows some return values for ***is_template()***:

```thingsdb,json_response
[
    is_template('Hello {name}'),
    is_template(template('Hello {name}')),
];
```

> Return value in JSON format

```json
[
    false,
    true
]
```
