---
title: "reset_counters"
weight: 332
---

Resets the [counters](../../node-api/counters) for the ThingsDB node you are connected too.
Other nodes are not affected.
This will set the `started_at` counter value to the current UNIX time-stamp in seconds and all other counters to `0` (zero).

This function does *not* generate a [change](../../overview/changes).

### Function

`reset_counters()`

### Arguments

None

### Return value

Returns `nil`.

### Example

> This code will reset the counters on a node:

```thingsdb,json_response,@n
// resets counters on the node in this scope
reset_counters();
```

> Return value in JSON format

```json
null
```
