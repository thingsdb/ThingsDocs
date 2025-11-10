---
title: "anonymous"
weight: 41
---

Anonymous type can be created to define the output value of things.

> Return value in JSON format

```thingsdb
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

``

### Related functions

Function | Description
------ | -----------
[ano](../../collection-api/ano) | Create an `anonymous` type from a [thing](../thing) using a function call.
[wrap](../thing/wrap) | Create an `anonymous` type from a [thing](../thing) using a function call.
[map_wrap](../list/map_wrap) _(on list)_ | Return a new [list](../list) with the Ids for all the *things* in the original list.
[map_wrap](../set/map_wrap) _(on set)_ | Return a [list](../list) with the Ids for all the *things* in the original *set*.