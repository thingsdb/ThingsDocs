---
title: "Optional Chaining"
weight: 30
---

ThingsDB double dot notation is called **optional chaining** and allows using a property or function call.

Using the double dot (`..`) notation simple stops evaluation if the value before the _double dot_ is either [nil](../../data-types/nil) or an [error](../../data-types/error).

For example:

```thingsdb,json_response
arr = [{
    key: 'a',
    value: 123,
}, {
    key: 'b',
    value: 456,
}];
arr.find(|o| o.key == 'a')..value;
```

The above simple returns the value you expect:

```json
123
```

But, what if we tried a key which does not exist?

```thingsdb,json_response
arr = [{
    key: 'a',
    value: 123,
}, {
    key: 'b',
    value: 456,
}];
arr.find(|o| o.key == 'c')..value;
```

Using just `.value` would raise an error but now `nil` is returned:

```json
null
```

This also works on an error.

```thingsdb,should_pass
// this property is only set if thing 12345 exists
try(thing(12345))..set('some_prop', 'some value');
```

The code above will not fail on `..set(..)` as it will not be called on an error.

