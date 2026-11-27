---
title: "render"
weight: 146
---

Renders a [template](..) using the current scope, unless a scope is provided.

This function does *not* generate a [change](../../../overview/changes), unless the template code itself modifies data in the target scope.

### Function

*template*.`render([scope])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
scope    | thing (optional) | The scope in which to evaluate the template. Defaults to the current scope if omitted.

### Return value

Returns the rendered `str` value.

### Example

> This code shows how to use `render()` with the current scope and with a custom scope:

```thingsdb,json_response
tpl = template('Hello {name}!');

name = 'Alice';
a = tpl.render();

b = tpl.render({name: 'Bob'});

[a, b];
```

> Return value in JSON format

```json
[
    "Hello Alice!",
    "Hello Bob!"
]
```