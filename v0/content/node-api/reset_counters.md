---
title: "reset_counters"
weight: 9
---

Resets the [counters](../../node-api/counters) for the ThingsDB node you are connected too.
Other nodes are not affected.

This function does *not* generate an [event](../../events).

### Function
`reset_counters();`

### Arguments
None

### Return value
Returns `nil`.

> This code will reset the counters on a node:

```thingsdb,json_response,@n
// resets counters on `localhost:9200`
reset_counters();
```

> Example return value in JSON format (the new collection id)

```json
null
```
