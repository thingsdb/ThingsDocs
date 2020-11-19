---
title: "event_id"
weight: 137
---

Returns the current event ID for the running query. The return value will be `nil` if the query does not require an event.

This function does *not* generate an [event](../../overview/events).

### Function

`event_id()`

### Arguments

None

### Return value

The current event ID or `nil` when the query has no event.

### Example

> Example using `event_id()`:

```thingsdb,json_response
event_id();  // nil, since no event is required
```

> Return value in JSON format

```json
null
```

> Using `event_id()` when the query *does* require an event:


```thingsdb,should_pass
wse(event_id());  // `wse` enforces an event
```

> Example return value in JSON format

```json
2593159
```