---
title: "dict"
weight: 62
---

A dictionary is similar to a [thing](../thing), but with key differences. Unlike a thing, a dictionary has no ID and accepts keys of type [int](../int), [uuid](../uuid) or [str](../str) without restrictions _(e.g. property `"#"` is reserved and cannot be used on a thing, but is valid as a dict key)_.

When returned in a client response, a dict is formatted as an array of key-value pairs (nested arrays). This preserves JSON compatibility, where integer keys are unsupported, and prevents potential duplicate keys caused by converting UUIDs to strings. Note that the order of the resulting array is not guaranteed and should be treated like an unordered map or object.

### Functions

Function | Description
------ | -----------
[clear](./clear) | Remove all items from the dict.
[copy](./copy) | Copy a dict.
[del](./del) | Delete an item from the dict by its key.
[dup](./dup) | Duplicate a dict.
[each](./each) | Iterate over all items in a dict.
[get](./get) | Return the value of an item by its key. If the key is not found, return nil unless an alternative default value is given.
[has](./has) | Determine if the dict has a given key.
[keys](./keys) | Return a list with all the keys of the dict.
[len](./len) | Return the number of items in the dict.
[map](./map) | Iterate over all items in a dict and return a list with the results of each iteration.
[restriction](./restriction) | Return the key/value restriction of the dict, or ["any", "any"] if no restriction is set.
[set](./set) | Set an item in a dict. If the key already exists, the old value will be overwritten.
[values](./values) | Return a list with all the values of the dict.

### Related functions

Function | Description
------ | -----------
[is_dict](../../collection-api/is/is_dict) | Test if a given value is of type dict.
