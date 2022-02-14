---
title: "add"
weight: 239
---

Adds a property to an existing [Type](../../../overview/type).

{{% notice info %}}
Since version **v0.9.2** an initial value is no longer required when having active instances of the given Type.
If the initial value is omitted, then ***a single*** default value according the [Type definition](../../..//overview/type/#definable-properties) will be created and applied to ***all instances***. See section ["init using callback"](#init-using-callback) for information on how to create a new initial value for each instance.
{{% /notice %}}

### Action

`mod_type(type, 'add', name, definition/closure, [init])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the [Type](../../../overview/type) where the property has to be added to.
`'add'` | str | Passing this argument will result in an *add* action.
name | str | Name of the property that has to be added.
definition/closure | str/closure | Type definition of the *property* or closure for the *method* that has to be added
init | any/closure | The default value to set on existing instances of this [Type](../../../overview/type). If a closure is used, then the closure will be called on each existing instance, see [init using callback](#init-using-callback). The `init` argument is only accepted when adding a new *property* on a type with [wrap-only](../wpo) mode disabled and must be omitted when adding a new *method* or changing a type with *wrap-only* mode enabled.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***add***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
    age: 'int'
});

// Add `hobbies` to type `Person`
mod_type('Person', 'add', 'hobbies', '[str]');

// Add a `whoami` method to type `Person`
mod_type('Person', 'add', 'whoami', |this| `My name is {this.name} and I am {this.age} years old.`);
```

> Return value in JSON format

```json
null
```

### Init using callback

Instead of a fixed initial value, a [closure](../../../data-types/closure) may be used. The closure will be called on each instance of the Type, with the instance as it's first argument.

{{% notice warning %}}
For types with *wrap-only* mode enabled there are no instances to migrate. Therefore it is not possible to use the `init` argument in combination with a *wrap-only* type.
{{% /notice %}}

The return value of the closure will be used as the new value, unless:

* `nil` is returned by the closure.
* The return value does not match the definition. In this case an [operation_err()](../../../errors/operation_err) is raised *after* `mod_type(..)` has finished.
* An error is raised inside the closure. In this case an [operation_err()](../../../errors/operation_err) is raised *after* `mod_type(..)` has finished.

In all three cases above, the value will be untouched after the callback. Thus, unless you have changed the property yourself, the default will be applied.

Suppose we want to add a `chat` property or type `Chat` to type `Room`:

```thingsdb,json_response
set_type('Chat', {
    messages: '[str]'
});

set_type('Room', {
    name: 'str'
});

.room_a = Room{
    name: 'room A'
};

.room_b = Room{
    name: 'room B'
};

/*
 * Suppose we want to add a `chat` property or type `Chat` to type `Room` and
 * used the following code:
 *
 *   mod_type('Room', 'add', 'chat', 'Chat');
 *
 * This would give `room A` and `room B` both the SAME instance of type Chat.
 * Thus when adding for example a message to room A, the message would also
 * appear in room B.
 *
 * This can be solved using a closure to assign a new instance to each instance of room.
 *
 *  mod_type('Room', 'add', 'chat', 'Chat', || Chat{});
 *
 * Alternatively, you could also perform some additional work based on the room, see code below:
 */


mod_type('Room', 'add', 'chat', 'Chat', |room| {
    room.chat = Chat{
        messages: [`Welcome in {room.name}`]
    };
    nil;  // Return `nil` since we have chosen to set `chat` inside the closure
});

.room_a.chat.messages;  // Return the chat messages of room A
```

> Return value in JSON format

```json
[
    "Welcome in room A"
]
```
