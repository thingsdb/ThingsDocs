---
title: "reset_counters"
date: 2019-10-14T09:43:17+02:00
weight: 4
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
