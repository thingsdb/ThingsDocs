---
title: "idx"
weight: 296
---

Enable or disable *auto-index* for an existing [Type](../../../overview/type).

When *auto-index* is enabled, this type will use an internal index for [type_all(..)](../../../collection-api/type_all) function calls, making them significatly faster, especially in collections with many things.

### Action

`mod_type(type, 'idx', mode)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where to set auto-index on or off.
`'idx'` | str | Passing this argument will result in a *set-auto-index action.
mode | bool | Enable or disable auto-index.

### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***idx***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
});

// Set type Person to hide the id
mod_type('Person', 'idx', true);

iris = Person{name: "Iris"};

type_all('Person');  // This will create an use cache, making the calls fast
```

> Return value in JSON format

```json
[
    {
        "name": "Iris"
    }
]
```