---
title: "ren"
weight: 267
---

Rename a property or method from an existing [Type](../../../overview/type).

### Action

`mod_type(type, 'ren', name, to)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where the property or method has to be modified from.
`'ren'` | str | Passing this argument will result in a *modify* action.
name | str | Name of the property or method that has to be modified.
to | str | New name for the property or method that has to be modified.

### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***ren***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    a: 'int',
});

// Rename `a` to `age`
mod_type('Person', 'ren', 'a', 'age');
```

> Return value in JSON format

```json
null
```
