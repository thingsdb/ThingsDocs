---
title: "filter"
date: 2019-10-23T13:54:00+02:00
weight: 2
---

When this method is used on a `thing`, then a new thing will be returned with only
the properties that pass the test.

This function does *not* generate an [event](../../../events).

### Function

*thing*.`filter(callback)`

### Arguments

The *callback* argument must be a `closure` which input values depend on the type the method is called on.

Iterable | Arguments   | Description
-------- | ----------- | -----------
thing    | name, value | Iterate over the thing properties. Both `name` and `value` are optional.

### Return value

A new `thing` with the properties that pass the test.
If no properties pass the test, a empty thing will be returned.

> This code shows an example using ***filter()***:

```thingsdb,json_response
user = {name: 'Iris', age: 6};

/*
 * Return a thing with only property age
 */

user.filter(|prop| (prop == 'age'));
```

> Return value in JSON format

```json
{
    "age": 6
}
```