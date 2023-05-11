---
title: "set"
weight: 172
---

Creates a new property on a [thing](..). If the property already exists then the old
property will be overwritten. This function is equal to an assignment except that
it can be used when the `name` of the property is dynamic.

This function generates a [change](../../../overview/changes).

### Function

*thing*.`set(name, value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
name | str (required) | The name of the property to set.
value | any (required)  | The value which will be assigned to the property.

### Return value

The value which will be assigned.

### Example

> This code shows how to use ***set()***:

```thingsdb,json_response
[
    .set('the_answer', 42),
    .the_answer,
];
```

> Return value in JSON format

```json
[
    42,
    42
]
```
