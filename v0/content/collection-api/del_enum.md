---
title: "del_enum"
weight: 120
---

Deletes an existing [enumerator type](../../data-types/enum).

It is not possible to delete a [enumerator type](../../data-types/enum) which is used by a
Type or if one of the enumerator members is still being used. See [example](#example) below.

This function generates an [event](../../overview/events).

### Function

`del_enum(enum)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | string | Name of the enumerator type to be deleted.

### Return value

The value `nil`.

### Example

> This code shows how to use ***del_enum()***:

```thingsdb,json_response
// Create type `B` which has a reference to type `A`
set_enum('Status', {
    OK: 0,
    NOK: -1,
});

status = enum('Status', 0);

// Cannot delete `Status` since one of the members is being used
assert(iserr(try(del_enum('Status'))));

// Assign `nil` to status so the enum member is released
status = nil;

// Now we can remove type `A`
del_enum('Status');
```

> Return value in JSON format

```json
null
```
