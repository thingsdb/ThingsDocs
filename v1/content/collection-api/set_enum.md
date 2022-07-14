---
title: "set_enum"
weight: 266
---

Creates a new [enumerator type](../../data-types/enum).

This function generates a [change](../../overview/changes).

### Function

`set_enum(enum, members)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | The name of the [enumerator type](../../data-types/enum) to create.
members | thing | Thing containing all the members to be set.

### Return value

The value `nil`.

### Example

> This code shows how to use ***set_enum()***:

```thingsdb,json_response
set_enum('Status', {
    OK: 0,
    NOK: -1
});
```

> Return value in JSON format

```json
null
```
