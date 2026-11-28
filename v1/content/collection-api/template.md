---
title: "template"
weight: 235
---

Returns a new [template](../../data-types/template) instance from a given string.

This function does *not* generate a [change](../../overview/changes).

### Function

`template(str)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`str` | `str` | The raw template string containing embedded ThingsDB expressions enclosed in curly brackets (`{...}`).

### Return value

Returns a new `template` value.

### Example

> This code creates a `template` and renders it using `.render()`:

```thingsdb,json_response
tpl = template('The sum of {a} plus {b} is {a + b}.');
a = 6; b = 7;
tpl.render();
```

> Return value in JSON format

```json
"The sum of 6 plus 7 is 13."
```