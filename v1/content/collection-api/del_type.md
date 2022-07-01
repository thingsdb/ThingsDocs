---
title: "del_type"
weight: 194
---

Deletes an existing [Type](../../overview/type).

It is not possible to delete a [Type](../../overview/type) which is used by another
Type. You should first change or delete the other Type before you are able to delete this Type.
See the example below.

{{% notice warning %}}
If there are still things of the Type you delete, then all things will be
converted to non-typed [things](../../data-types/thing). No properties will be removed
in this process. With [type_count(..)](../type_count)
you can view the number of things of a certain Type.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`del_type(type)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | string | Name of the Type to be deleted.

### Return value

The value `nil`.

### Example

> This code shows how to use ***del_type()***:

```thingsdb,json_response
// Create type `A`
new_type('A');

// Create type `B` which has a reference to type `A`
set_type('B', {
    a: 'A'
});

// Cannot delete `A` since it is referenced by type `B`.
assert(is_err(try(del_type('A'))));

// First change type `B`
mod_type('B', 'mod', 'a', 'thing');

// Now we can remove type `A`
del_type('A');
```

> Return value in JSON format

```json
null
```
