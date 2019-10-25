---
title: "wse"
date: 2019-10-14T10:06:27+02:00
weight: 42
---

Stored closures which can potentially make changes to ThingsDB are called
*closures with side effects* and must be wrapped with the `wse(..)` function.

This allows ThingsDB before running the query to make an event.
You should not wrap `wse` around all closures since this would unnecessary
create events when they may not be required.

This function generates an [event](../../events).

### Function

`wse(statement)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
statement | any | Statement or block to wrap.

### Return value

Return value of the given statement.

> This code shows an example usage for ***wse()***:

```thingsdb,json_response
wse({
    x = 0;
    a = |v| x += v;
    [1 ,2 ,3, 4].map(a);  /* without wse() this would raise an error */
    x;
});
```

> Return value in JSON format

```json
10
```
