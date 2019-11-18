---
title: "del_type"
weight: 117
---

Deletes an existing [Type](../../data-types/type).

It is not possible to delete a [Type](../../data-types/type) which is used by another
type. You should first change or delete the other type before you are able to delete this type.
See the example below.

{{% notice warning %}}
If there are still instances of the `type` you delete, then all instances will be
converted to normal [things](../../data-types/thing). No properties will be removed
in this process. With [type_count(..)](../type_count)
you can view the number of instances of a certain type.
{{% /notice %}}

This function generates an [event](../../events).

### Function

`del_type(type_name)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type_name | string | Name of the Type to be deleted.

### Return value

The value `nil`.

> This code shows how to use ***del_type()***:

```thingsdb,json_response
// Create type `A`
new_type('A');

// Create type `B` which has a reference to type `A`
set_type('B', {
    a: 'A'
});

// Cannot delete `A` since it is referenced by type `B`.
assert(iserr(try(del_type('A'))));

// First change type `B`
mod_type('B', 'mod', 'a', 'thing');

// Now we can remove type `A`
del_type('A');
```

> Return value in JSON format

```json
null
```
