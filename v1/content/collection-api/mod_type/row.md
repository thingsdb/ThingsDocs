---
title: "row"
weight: 323
---

The `row` action configures or disables the *wrap-as-row* behavior for a specific type.

When *wrap-as-row* is enabled by providing a list of column names, calling `.wrap()` on an instance of the type returns an array of values corresponding to those fields or methods in the specified order.

Passing `nil` disables *wrap-as-row*.

### Action

`mod_type(type, 'row', columns)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type to modify.
`'row'` | str | Passing this argument will result in a *wrap-as-row* action.
columns | list / nil | List with columns names. Each column must refer to either a field or method. At least one column is required. Use `nil` to disable *wrap-as-row*.


### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***row***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    id: '#',
    name: 'str',
});

mod_type('Person', 'row', ['id', 'name']);
Person{
    name: 'Alice',
}.wrap();
```

> Return value in JSON format

```json
[null, "Alice"]
```
