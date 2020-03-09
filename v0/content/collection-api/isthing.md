---
title: "isthing"
weight: 130
---

This function determines whether the provided value is a [thing](../../data-types/thing) or not.

{{% notice note %}}
[Type](../../data-types/type) instances are also things, so this function returns `true` for a Type instance as well.
{{% /notice %}}

This function does *not* generate an [event](../../overview/events).

### Function

`isthing(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | any (required) | The value to be tested.

### Return value

Returns `true` if the given value is a thing, else it returns `false`.

### Example

> This code shows some return values for ***isthing()***:

```thingsdb,json_response
new_type('A');
[
    isthing( {} ),
    isthing( A{} ),
    isthing( [] ),
];
```

> Return value in JSON format

```json
[
    true,
    true,
    false
]
```
