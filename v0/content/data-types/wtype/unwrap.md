---
title: "unwrap"
weight: 103
---

Unwrap a [wrapped](../) thing.

### Function

*<Type>*.`unwrap()`

### Arguments

None

### Return value

Returns the wrapped [thing](../../thing).

### Example

> This code shows an example using ***unwrap()***:

```thingsdb,should_pass
// Create a Type to return just an email field.
set_type('_Email', {email: 'str'});

// Store a thing
.joente = {
    name: 'Jeroen van der Heijden',
    email: 'jeroen@transceptor.technology',
    gender: 'male',
};

// Wrap `joente` with the `_Email` type.
.w = .joente.wrap('_Email');

// Return the original `thing`
.w.unwrap();
```

> Example return value in JSON format

```json
{
    "#": 42,
    "name": "Jeroen van der Heijden",
    "email": "jeroen@transceptor.technology",
    "gender": "male"
}
```
