---
title: "enum"
weight: 186
---

Returns a [enum](../../data-types/enum) member from a given value.
A [lookup_err()](../../errors/lookup_err) is raised if either the enum or value is not found.

This function does *not* generate a [change](../../overview/changes).

### Function

`enum(enum, [value])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str (required) | The name of the enumeration type.
value | any (optional) | The value to search the enum member for. If omitted, the default member is returned.

### Return value

Member within the given enum equal to the given value.

### Example

> This code shows some return values for ***enum(..)***:

```thingsdb,json_response
set_enum('Status', {
    OK: 0,
    NOK: -1
});

// get the `Status` member with value `0`
status = enum('Status', 0);

status.name();  // return the `name` of the enum member
```

> Return value in JSON format

```json
"OK"
```
