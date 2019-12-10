---
title: "counters"
weight: 139
---

Returns `counters` for the ThingsDB node in the selected scope. Counters start all at zero when ThingsDB
is started, or when the counters are reset by using [reset_counters()'](../../node-api/reset_counters).

Counters give information about things, queries and events. If you suspect failed queries, then
counters might provide you with more information.

Counter | Description
------- | -----------
average_event_duration | The average event duration in seconds.
average_query_duration | The average query duration in seconds.
events_committed | Events committed since last counters reset.
events_failed | Failed events. This is a critical counter which should be 0.
events_killed | Killed events took too long for receiving the `READY` status. These event may be processed later.
events_quorum_lost | Number of times a quorum was not received.
events_skipped | Events which cannot be committed since an event with a higher `id` is already processed. These events are moved to a skipped queue.
events_unaligned | Number of times an event cannot be pushed to the end of the queue and needs re-ordering.
events_with_gap | Events which are committed but at least one event `id` was skipped.
garbage_collected | Number of things which are garbage collected.
longest_event_duration | Longest event duration, in seconds.
longest_query_duration | Longest query duration, in seconds.
queries_success | Number of queries where this node acted as the master node and the query has successful finished.
queries_with_error | Number of queries where this node acted as the master node but the query has returned with an error.
watcher_failed | The value is increased if an update could not be forwarded to a registered watcher.


This function does *not* generate an [event](../../overview/events).

### Function
`counters();`

### Arguments
None

### Return value
Returns the current counter values.

### Example

> This code will return node counter values:

```thingsdb,should_pass,@n
// Returns the current counters the the node in this scope
counters();
```

> Example return value in JSON format

```json
{
    "average_event_duration": 0.0002218758461538461,
    "average_query_duration": 0.00007062491772151898,
    "events_committed": 26,
    "events_failed": 0,
    "events_killed": 0,
    "events_quorum_lost": 0,
    "events_skipped": 0,
    "events_unaligned": 0,
    "events_with_gap": 0,
    "garbage_collected": 0,
    "longest_event_duration": 0.000295981,
    "longest_query_duration": 0.000152664,
    "queries_success": 159,
    "queries_with_error": 0,
    "watcher_failed": 0
}
```
