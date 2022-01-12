---
title: "wpo"
weight: 244
---

Enable or disable *wrap-only* mode for an existing [Type](../../../overview/type).

When wrap-only mode is enabled, no instances of the type can be created and the type
can not be used by other type unless that type is also in wrap-only mode. The only purpose of a type in wrap-only mode is to [wrap](../../../data-types/thing/wrap) things with but this gives you the assurance that no data is created using this type.

#### Enable wrap-only mode

To enable wrap-only mode, make sure no instances of this type exist, and also be sure that no *other* type without wrap-only mode is dependent on the type you want to change. Loosely dependencies, like *nillable (`"Type?"`)*, *array-of (`"[Type]"`)* or *set-of (`"{Type}"`)* dependencies are allowed.

#### Disable wrap-only mode

To disable wrap-only mode, make sure the type has no dependencies to type with *wrap-only* mode enabled. Loosely dependencies, like *nillable (`"Type?"`)*, *array-of (`"[Type]"`)* or *set-of (`"{Type}"`)* dependencies are allowed.

### Action

`mod_type(type, 'wpo', mode)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where to set the wrap-mode for.
`'wpo'` | str | Passing this argument will result in a *set-wrap-mode* action.
mode | bool | Enable or disable wrap-mode.

### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***wpo***:

```thingsdb,should_err
// Create type `Person`
set_type('Person', {
    name: 'str',
    a: 'int',
});

// Set type Person in wrap-only mode
mod_type('Person', 'wpo', true);

// Raises a type error
Person{};
```

Raises a [type_err()](../../../errors/type_err): *type `Person` has wrap-only mode enabled*