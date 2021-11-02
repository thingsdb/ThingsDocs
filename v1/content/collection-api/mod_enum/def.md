---
title: "def"
weight: 222
---

Set a member from an existing [enumerator type](../../../data-types/enum) as default member.
The default member is also selected when a instance of a [Type](../../../overview/type) is created using the enumerator as a required property.


### Action

`mod_enum(enum, 'def', name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | Name of the [enumerator type](../../../data-types/enum) where the member has to be removed from.
`'def'` | str | Passing this argument will result in a *set default* action.
name | str | Name of the member to set as default.

### Return value

The value `nil`.

### Example

> This code shows how to use the action ***def***:

```thingsdb,json_response
set_enum('Color', {
    RED: '#f00',
    GREEN: '#0f0',
    BLUE: '#00f'
});

// set GREEN as the default color
mod_enum('Color', 'def', 'GREEN');

enum('Color').name();  // color now defaults to GREEN
```

> Return value in JSON format

```json
"GREEN"
```
