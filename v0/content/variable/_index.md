---
title: "Variable"
weight: 8
chapter: true
---

# Variable

Can be used to assign a value to a variable which can be used within a query.

Variable can be created with `READ` privileges since they do not modify
the collection data.

To create a variable, just use a valid [name](../names).

Some valid examples:

- `_ = ...`
- `tmp = ...`
- `var1 = ...`

> This code uses a variable:

```thingsdb,json_response
a = 'This is a variable!!!';
b = 'Hello';
{
    /* This will create a new variable `a` within this scope */
    a = 'New variable within this block';

    /* This will update the global variable `b` */
    b += ' World';
};
[a, b];
```

> Return value in JSON format

```json
[
    "This is a variable!!!",
    "Hello World"
]
```
