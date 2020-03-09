---
title: "Conditional ternary operator"
weight: 100
---

The conditional operator returns one of two values based on the logical value of the condition.

### Syntax:

`expression ? if-true : if-false`

> Conditional (ternary) operator examples:

```thingsdb,json_response
2 > 1  ? 'two is greater than one' : 'two is less than one';
```

> Return value in JSON format

```json
"two is greater than one"
```

It is possible to use block scopes for the `if-true` and `if-false` part for the conditional operator.

> For example:

```thingsdb,syntax_only
.sessions.len() < .licenses ? {
    // we have a license, do something...
    .sessions.add(Session{
        timestamp: now()
    });
} : {
    // no licenses left
    raise('no licenses left');
}
```
