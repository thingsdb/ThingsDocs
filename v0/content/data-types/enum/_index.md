---
title: "enum"
weight: 36
---

Enumerators are a set of unique names coupled to a unique set of values. ThingsDB support enumerators for type `int`, `float`, `str`, `bytes` and `thing`, where all members
must have the same type. Thus, it is not possible to have an enum type with for example both values of type `int` and `str`. Enumerators with type `thing` may contain `things`
using different [Type](../type) as each instance of a Type is still a [thing](../thing).


### Functions

Function | Description
------ | -----------
[name](./name) | Return the name of the enum member.
[value](./value) | Return the value of the enum member.


### Related functions

Function | Description
------ | -----------
[del_enum](../../collection-api/del_enum) | Delete an enumerator type.
[enum](../../collection-api/enum) | Get an enum member by value.
[enum_info](../../collection-api/enum_info) | Return info about the enumerator type.
[enums_info](../../collection-api/enums_info) |Return info about all the enumerator types in the current scope.
[has_enum](../../collection-api/has_enum) | Determine if the current scope has a given enumerator type.
[isenum](../../collection-api/isenum) | Test if a given value is a member of an enumerator type.
[mod_enum](../../collection-api/mod_enum) | Modify an existing enumerator type.
[set_enum](../../collection-api/set_enum) | Create a new enumerator type.


### Example

```thingsdb,json_response
// Create an enumeration type using `set_enum`
set_enum('Severity', {
    CRITICAL: 1,
    MAJOR: 2,
    MINOR: 3
});

// Get a member by name
a = Severity{CRITICAL};

// Or, dynamically by name
b = Severity{||'MAJOR'};

// Get a member by it's value
c = enum('Severity', 3);

// Variable `a`, `b` and `c` are all members of type `Severity`
assert( type(a) == 'Severity' );

// The actual value can be accessed via the `.value()` function
assert( b.value() == 2 );

// Or, the name can be returned using the `.name()` function
assert( c.name() == 'MINOR');

// The value of the members will be returned in a response
[a, b, c];
```

> Return value in JSON format

```json
[
    1,
    2,
    3
]
```