---
title: "enum"
weight: 51
---

Enumerators are a set of unique names coupled to a unique set of values. ThingsDB support enumerators for type `int`, `float`, `str`, `bytes` and `thing`, where all members
must have the same type. Thus, it is not possible to have an enum type with for example both values of type `int` and `str`. Enumerators with type `thing` may contain both [things](../thing) and [typed things](../typed)
as they are both compatible with type [thing](../thing).

In addition to values, methods on enumerators can also be defined as [closures](../closure). When a method is called, the first argument is the enum member. This can be useful for organizing code.


### Functions

Function | Description
------ | -----------
[name](./name) | Return the name of the enum member.
[value](./value) | Return the value of the enum member.


### Related functions

Function | Description
------ | -----------
[del_enum](../../collection-api/del_enum) | Delete an enumerator type.
[enum](../../collection-api/enum) | Get an enumerator member by value.
[enum_info](../../collection-api/enum_info) | Return info about the enumerator type.
[enums_info](../../collection-api/enums_info) |Return info about all the enumerator types in the current scope.
[has_enum](../../collection-api/has_enum) | Determine if the current scope has a given enumerator type.
[is_enum](../../collection-api/is/is_enum) | Test if a given value is a member of an enumerator type.
[mod_enum](../../collection-api/mod_enum) | Modify an existing enumerator type.
[rename_enum](../../collection-api/rename_enum) | Rename the enumerator type.
[set_enum](../../collection-api/set_enum) | Create a new enumerator type.

### Example

```thingsdb,json_response
// Create an enumeration type using `set_enum`
set_enum('Severity', {
    CRITICAL: 1,
    MAJOR: 2,
    MINOR: 3,
    DEBUG: 4,
    str: |this| `{this.name()} ({this})`,
});

// Get a member by name
a = Severity{CRITICAL};

// Get a member by value
b = Severity(2);  // MAJOR

// Dynamically by name
c = Severity{||'MINOR'};

// Or, dynamically both by name and value
d = enum('Severity', 4);  // DEBUG

// Variable `a`, `b`, `c` and `d` are all members of type `Severity`
type_assert(a, 'Severity');
type_assert(b, 'Severity');
type_assert(c, 'Severity');
type_assert(d, 'Severity');

// The actual value can be accessed via the `.value()` function
assert( b.value() == 2 );

// Or, the name can be returned using the `.name()` function
assert( c.name() == 'MINOR');

// Methods can be defined. In the example we defined a method `str` for a string representation
assert( d.str() == 'DEBUG (4)');

// The value of the members will be returned in a response
[a, b, c, d];
```

> Return value in JSON format

```json
[
    1,
    2,
    3,
    4
]
```

