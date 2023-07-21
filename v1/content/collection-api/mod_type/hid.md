---
title: "hid"
weight: 263
---

Enable or disable *hide-id* for an existing [Type](../../../overview/type).

When _hide_id_ is enabled, this type will not return the Id property to the client unless _deep_ is equal to zero (0) in which case _only_ the Id is returned. This last behavior is different from the `NO_IDS` flag which can be used for example with the [return](../../../overview/statements/#return-flags) statement. _(The `NO_IDS` flag would return empty things when deep is 0)_

### Action

`mod_type(type, 'hid', mode)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type where to set hide-id on or off.
`'hid'` | str | Passing this argument will result in a *set-hide_id* action.
mode | bool | Enable or disable hide-id.

### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***hid***:

```thingsdb,json_response
// Create type `Person`
set_type('Person', {
    name: 'str',
});

// Set type Person to hide the id
mod_type('Person', 'hid', true);

.iris = Person{name: "Iris"};

.iris; // Notice that Iris is stored but still is returned without Id.
```

> Return value in JSON format

```json
{
    "name": "Iris"
}
```