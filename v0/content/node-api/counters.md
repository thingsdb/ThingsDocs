---
title: "counters"
weight: 84
---

Returns `counters` for the ThingsDB node you are connected too. Counters start all at zero when ThingsDB
is started, or when the counters are reset by using [reset_counters()'](../../node-api/reset_counters).

Counters give information about things, queries and events. If you suspect failed queries, then
counters might provide you with more information.

Counter | Description
------- | -----------
average_event_duration | The average event duration in seconds.
events_committed | Events committed since last counters reset.
events_failed | Failed events. This is a critical counter which should be 0.
events_killed | Killed events took too long for receiving the `READY` status. These event may be processed later.
events_quorum_lost | Number of times a quorum was not received.
events_skipped | Events which cannot be committed since an event with a higher `id` is already processed. These events are moved to a skipped queue.
events_unaligned | Number of times an event cannot be pushed to the end of the queue and needs re-ordering.
events_with_gap | Events which are committed but at least one event `id` was skipped.
garbage_collected | Number of things which are garbage collected.
longest_event_duration | Longest event duration, in seconds.
queries_success | Number of queries where this node acted as the master node and the query has successful finished.
queries_with_error | Number of queries where this node acted as the master node but the query has returned with an error.

This function does *not* generate an [event](../../events).

### Function
`counters();`

### Arguments
None

### Return value
Returns the current counter values.

### Example

> This code will return node counter values:

```thingsdb,should_pass,@n
// returns counters for `localhost:9200`
counters();
```

> Example return value in JSON format

```json
{
    "average_event_duration": 3.368566710075053e-05,,
    "events_committed": 80352,
    "events_failed": 0,
    "events_killed": 0,
    "events_quorum_lost": 0,
    "events_skipped": 0,
    "events_unaligned": 0,
    "events_with_gap": 0,
    "garbage_collected": 0,
    "longest_event_duration": 3.508100053295493e-05,
    "queries_received": 130944
}
```
