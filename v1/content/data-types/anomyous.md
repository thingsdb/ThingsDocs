---
title: "anonymous"
weight: 42
---

Anonymous types are used to define a restricted structural definition of data, used to control the exact output structure.

The anonymous literal syntax `&{...}` is the preferred method for defining anonymous types:

```thingsdb,syntax_only
&{
    field_1: 'type_def_1',
    field_2: 'type_def_2',
    // ...
}
```

As an alternative, the [ano(..)](../../collection-api/ano) function can be used.
This is generally only useful when you need to construct the type definition dynamically at runtime using input or program logic.

### Usage Example

In this example, an instance of the full `User` type is created, but the [wrap](../thing/wrap) method uses an anonymous type to ensure only specific fields (`id`, `name`, `email`) are returned, effectively hiding the sensitive `password_hash`.

```thingsdb,should_pass
// User type with three field:
set_type('User', {
    name: 'str',
    email: 'str',
    password_hash: 'str',
});

// Create an instance of "User"
.user = User{
    name: 'Jeroen van der Heijden',
    email: 'jeroen@cesbit.com',
    password_hash: 'SGVsbG8gVGhpbmdzREIhCg==',
};

// Output only the `name`, `user` and generated `id` attached to the user instance
.user.wrap(&{
    id: '#',
    name: 'str',
    email: 'str'
});
```

> Possible return value in JSON format
```json
{
    "id": 12345,
    "name": "Jeroen van der Heijden",
    "email": "jeroen@cesbit.com"
}
```
### Complex Structures

Anonymous types support all standard type definitions, including nested structures, arrays, and enumerator references.

```thingsdb,should_pass
&{
    id: '#',
    checks: [{
        type: '*enum',  // exposes an enumerator type instance by its name
        options: {
            is_silent: 'bool',
            interval: 'int',
        },
    }],
}
```

For a comprehensive guide on all available type definitions and their syntax, please refer to the [type overview page](../../overview/type).

### Related functions

Function | Description
------ | -----------
[ano](../../collection-api/ano) | Create an `anonymous` type from a [thing](../thing) using a function call.
[wrap](../thing/wrap) | Wrap the *thing* with a [Type](../../overview/type).
[map_wrap](../list/map_wrap) _(on list)_ | Return a new [list](../list) with the Ids for all the *things* in the original list.
[map_wrap](../set/map_wrap) _(on set)_ | Return a [list](../list) with the Ids for all the *things* in the original *set*.