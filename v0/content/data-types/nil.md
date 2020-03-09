---
title: "nil"
weight: 58
---

Probably the most simple type, it can be used as *no value*.

It might be convenient to use `nil` as the last statement in a query to prevent
returning data which is not required. See the code example.

> This code uses `nil` to prevent returning unused data:

```thingsdb,json_response
my_array = [1, 2, 3, 42];
nil;  /* without nil, the array above would be returned */
```

> Return value in JSON format

```json
null
```
