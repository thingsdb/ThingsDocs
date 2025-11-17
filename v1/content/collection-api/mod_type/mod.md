---
title: "mod"
weight: 296
---

Modifies the type definition of a property or the closure of a method from an existing [Type](../../../overview/type).
It is not possible to convert a *property* to a *method* or the other way around.

{{% notice note %}}
Without an additional `callback` it is possible to modify to a less 'strict' definition.
So for example, `age: 'int'` can become `age: 'int?'`, but not the other way around.
Since version **v0.9.3** it is possible to migrate to a more strict or completely different definition by using an additional
callback closure for generating new values.
{{% /notice %}}

### Action

`mod_type(type, 'mod', name, definition, [callback])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where the property has to be modified from.
`'mod'` | str | Passing this argument will result in a *modify* action.
name | str | Name of the property or method that has to be modified.
definition/closure | str/closure | New type definition of the property or closure for the method that has to be modified.
callback | closure | The closure will be called on each existing instance and can be used to set a new value, see [modify using callback](#modify-using-callback). The `callback` argument is only accepted when modifying a *property* on a type with [wrap-only](../wpo) mode disabled and must be omitted when modifying a *method* or changing a type with *wrap-only* mode enabled.


### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***mod***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    age: 'int',
    whoami: |this| `My name is {this.name} and I am {this.age} years old.`
});

// Make `age` nillable
mod_type('Person', 'mod', 'age', 'int?');

// Change the `whoami` method
mod_type('Person', 'mod', 'whoami', |this| {
    is_int(this.age)
        ? `My name is {this.name} and I am {this.age} years old.`
        : `My name is {this.name} and my age is a well kept secret.`;
});
```

> Return value in JSON format

```json
null
```

### Modify using callback

If you want to migrate an exiting property definition to a complete different or more strict definition, an addition [closure](../../../data-types/closure) argument *must* be used to generate new values for existing instances *(with the exception of types with wrap-only mode enabled)*.

{{% notice warning %}}
For types with *wrap-only* mode enabled there are no instances to migrate and therefore the `callback` argument cannot be used.
{{% /notice %}}

The return value of the closure will be used as the new value, unless:

* `nil` is returned by the closure.
* The return value does not match the new definition. In this case an [operation_err()](../../../errors/operation_err) is raised *after* `mod_type(..)` has finished.
* An error is raised inside the closure. In this case an [operation_err()](../../../errors/operation_err) is raised *after* `mod_type(..)` has finished.

In all three cases above, the value will be untouched after the callback *unless* the existing property does not match with the new definition. In the latter case, a default value will be applied *after* the callback has finished.

During the migration, each instance has *any* definition for the property which is being modified. This is done by ThingsDB so we ensure that both the *old* value, and the *new* value will match the definition. This means that when the callbacks are executed, everything may be attached to the property. This value will be corrected by ThingsDB if there is no match between the value and the new definition.

Suppose we want to modify a `chat` property on type `Room` from definition `"str"` to definition `"Chat"`:

```thingsdb,json_response
set_type('Room', {
    chat: 'str'
});

my_room = Room{
    chat: 'My Chat Room!'
};

// Create a new Chat type
set_type('Chat', {
    messages: '[str]',
    name: 'str',
});

// Replace the `chat` string with the `Chat` type.
// As name for the new Chat type we apply the `old` chat string
mod_type('Room', 'mod', 'chat', 'Chat', |room| Chat{name: room.chat});

my_room.chat;  // Return my chat room
```

> Return value in JSON format

```json
{
    "messages": [],
    "name": "My Chat Room!"
}
```
