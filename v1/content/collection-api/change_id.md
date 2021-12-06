---
title: "change_id"
weight: 180
---

Returns the current change Id for the running query. The return value will be `nil` if the query does not require a *change*.

This function does *not* generate a [change](../../overview/changes).

### Function

`change_id()`

### Arguments

None

### Return value

The current change Id or `nil` when the query does not require a *change*.

### Example

> Example using `change_id()`:

```thingsdb,json_response
change_id();  // nil, since no change is required
```

> Return value in JSON format

```json
null
```

> Using `change_id()` when the query *does* require an change:


```thingsdb,should_pass
wse(change_id());  // `wse` enforces a change
```

> Example return value in JSON format

```json
2593159
```