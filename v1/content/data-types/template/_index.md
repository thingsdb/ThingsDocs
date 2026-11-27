---
title: "template"
weight: 145
---

A `template` stores a compiled template string that can be evaluated and rendered on demand using the `.render()` method. Unlike [template strings](../../overview/template-strings), which are evaluated immediately, a `template` instance can be stored as a property and rendered later in the current or a provided scope.

A `template` can be created using the [template](../../collection-api/template) function.

When a `template` is returned directly from a query (without calling [render](./render)), it serializes as its raw template string.

> This code creates a `template` and returns its raw string representation:

```thingsdb,json_response
template('Hello {name}!');
```

> Return value in JSON format:

```json
"Hello {name}!"
```

### Example

> This code creates a *template* property *greeting* on the root of a collection and renders it:

```thingsdb,json_response
.greeting = template('Hello {name}!');
name = 'World';
.greeting.render();
```

> Return value in JSON format:

```json
"Hello World!"
```

### Functions

Function | Description
------ | -----------
[len](./len) | Return the length of the raw template.
[render](./render) | Render a template using the current scope, unless a scope is provided.