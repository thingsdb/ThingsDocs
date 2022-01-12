---
title: "filter"
weight: 150
---

The function returns a new thing with properties that pass the test.

This function does *not* generate a [change](../../../overview/changes).

### Function

*thing*.`filter(callback)`

### Arguments

| Argument | Type               | Description                       |
| -------- | ------------------ | --------------------------------- |
| callback | closure (required) | Closure to execute on each value. |

Explanation of the *callback* argument:

Iterable | Arguments   | Description
-------- | ----------- | -----------
thing    | name, value | Iterate over the thing properties. Both `name` and `value` are optional.

### Return value

A new `thing` with the properties that pass the test.
If no properties pass the test, a empty thing will be returned.

### Example

> This code shows an example using ***filter()***:

```thingsdb,json_response
user = {name: 'Iris', age: 6};

/*
 * Return a thing with only property age
 */

user.filter(|prop| prop == 'age');
```

> Return value in JSON format

```json
{
    "age": 6
}
```
