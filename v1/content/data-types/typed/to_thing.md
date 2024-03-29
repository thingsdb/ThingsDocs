---
title: "to_thing"
weight: 185
---

Converts a *[typed](../../typed)* thing into a *[thing](../../thing)*.

This function can only be used if the [type](../../../overview/type) of the typed thing is not required by *any* other type (including a self dependency). If the type *is* dependent by another type, then ThingsDB has no way to tell if it is allowed to do the conversion.

This function generates a [change](../../../overview/changes).

### Function

*typed-thing*.`to_thing()`

### Arguments

None

### Return value

Returns `nil` when successful.

### Example

> This code converts a typed thing to a thing:

```thingsdb,json_response
// Create a new type `Example`
new_type('Example');

// create a instance of Example
sample = Example{};

// this will raise an error as type Example does not allow property `name`
is_err(try(sample.name = 'Test'));

// convert to a thing
sample.to_thing();

// we now can set any property we like
sample.name = 'Test';

sample;
```

> Return value in JSON format

```json
{
    "name": "Test"
}
```
