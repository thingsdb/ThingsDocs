---
title: "Variable"
weight: 31
---

Can be used to assign a value to a variable which can be used within a query.

Variable can be created with `QUERY` privileges since they do not modify
the collection's data.

To create a variable, just assign a value to a valid [name](../names).

Some valid examples:

- `_ = ...`
- `tmp = ...`
- `var1 = ...`

Variables created within a closure become *local*. They can only be used within the closure body. See the example below:

```thingsdb,json_response
a = 'This is a variable!!!';
b = 'Hello';
(||{
    /* This will create a new, local, variable `a` */
    a = 'New variable within this block';

    /* This will update the global variable `b` */
    b += ' World';
}).call();
[a, b];
```

> Return value in JSON format

```json
[
    "This is a variable!!!",
    "Hello World"
]
```

## Injecting variable

When running a query to ThingsDB, it is possible to *inject* variables into the code.
This is easy, safe, and in some cases even necessary when for example inserting binary data.

> Python example:

```python
# inject a variable into the code:
client.query('.a = a;', a=1)
```

### Prevent code injection

Consider you have some user input which is supposed to contain a *name*, and you want to store that *name* in ThingsDB.

```python
# Variable `user_input` is supposed to contain a name like `Bob`
client.query(f'.name = "{user_input}";')
```

Instead of a *name*, a user could insert something like this: `Bob"; .XXX = "This system is hacked!`. This would result in the following query statement:

```thingsdb,should_pass
.name = "Bob"; .XXX = "This system is hacked!";
```

This is very dangerous and definitely not what we want but luckily ThingsDB has a simple solution: *variable injection*

```python
client.query('.name = inp;', inp=user_input)
```

Using *variable injection* we can parse user input in a safe and secure way to ThingsDB.

