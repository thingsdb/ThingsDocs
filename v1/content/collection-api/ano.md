---
title: "ano"
weight: 210
---

Create an [anonymous](../../data-types/anomyous) type from a given [thing](../../data-types/thing).

{{% notice tip %}}
We recommend using the [anonymous](../../data-types/anomyous) syntax `&{...}`. Unlike the `ano(...)` function, the `&{...}` literal syntax allows ThingsDB to perform compile-time optimization.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`ano(value)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
value | thing | The thing representing the [anonymous](../../data-types/anomyous) type.

### Return value

Return with an [anonymous](../../data-types/anomyous) type.

### Example

> This code shows how the `ano` function can be used.

```thingsdb,json_response
filter = ano({
    name: 'str',
    email: 'str'
});

{
    name: 'Jeroen van der Heijden',
    email: 'jeroen@cesbit.com',
    password_hash: 'SGVsbG8gVGhpbmdzREIhCg==',
}.wrap(filter);
// Output only the `name`, `user`
```

> Return value in JSON format

```json
{
    "name": "Jeroen van der Heijden",
    "email": "jeroen@cesbit.com"
}
```
