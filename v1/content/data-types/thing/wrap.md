---
title: "wrap"
weight: 188
---

Wrap a thing with a [Type](../../../overview/type) to filter out properties, while preserving the Id.
A wrapped *thing* inherits the [methods](../../../overview/type/#methods) from the *type* it is wrapped with.

For a more advanced example using [wrap()](..) and [unwrap()](../../wtype/unwrap) see [\<Type\>](../../wtype/#example).

### Function

*thing*.`wrap([Type])`

### Arguments

Argument | Arguments     | Description
-------- | ------------- | -----------
Type     | str (optional)| Type's name to wrap the thing with. If not given, the thing will be wrapped with its own type.

### Return value

A [wrapped](../../wtype) thing.

### Example

> This code shows an example using ***wrap()***:

```thingsdb,should_pass
// Create a Type to return just an email field.
set_type('_Email', {email: 'str'});

// Store a thing
.joente = {
    name: 'Jeroen van der Heijden',
    email: 'jeroen@cesbit.com',
    gender: 'male',
};

// Return the email field and Id (#)
.joente.wrap('_Email');
```

> Example return value in JSON format

```json
{
    "#": 42,
    "email": "jeroen@cesbit.com"
}
```
