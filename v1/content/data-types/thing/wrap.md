---
title: "wrap"
weight: 191
---

Wrap a thing with a [Type](../../../overview/type) to filter out properties, while preserving the Id.
A wrapped *thing* inherits the [methods](../../../overview/type/#methods) from the *type* it is wrapped with.

For a more advanced example using [wrap()](..) and [unwrap()](../../wtype/unwrap) see [\<Type\>](../../wtype/#example).

### Function

*thing*.`wrap([Type])`

### Arguments

Argument | Arguments     | Description
-------- | ------------- | -----------
Type     | str/anonymous (optional)| Type's name or [anonumous](../../anomyous) type to wrap the thing with. If not given, the thing will be wrapped with its own type.

### Return value

A [wrapped](../../wtype) thing.

### Example

> This code shows an example using ***wrap()***:

```thingsdb,json_response
// Create a Type to return just an email field.
set_type('_Email', {email: 'str'}, WPO|HID);

user = {
    name: 'Jeroen van der Heijden',
    email: 'jeroen@cesbit.com',
    gender: 'male',
};

// Return the email field
user.wrap('_Email');
```

> Return value in JSON format

```json
{
    "email": "jeroen@cesbit.com"
}
```

> Same example using an **anonymous** type:

```thingsdb,should_pass
user = {
    name: 'Jeroen van der Heijden',
    email: 'jeroen@cesbit.com',
    gender: 'male',
};

// Return the email field
user.wrap(&{email: 'str'});
```

> Return value in JSON format

```json
{
    "email": "jeroen@cesbit.com"
}
```
