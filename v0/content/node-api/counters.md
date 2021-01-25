---
title: "counters"
weight: 222
---

Returns `counters` for the ThingsDB node in the selected scope. Counters start all at zero when ThingsDB
is started, or when the counters are reset by using [reset_counters()'](../reset_counters).

Counters give information about things, queries and events. If you suspect failed queries, then
the counters might provide you with more information.

Counter | Description
------- | -----------
average_event_duration | The average [event](../../overview/events) duration in seconds. Event duration is measured from the time an event is created *(before the final ID is assigned)*, until the actual event is committed to ThingsDB.
average_query_duration | The average query duration in seconds. Query duration is measured from the time a query *(or procedure run)* request is unpacked, until the response is created to send back to the client.
events_committed | [Events](../../overview/events) committed since last the counters reset.
events_failed | Failed events. This is a *critical* counter which should be `0`.
events_killed | Killed events took too long for receiving the `READY` status. These events may be processed later.
events_quorum_lost | Number of times this node did not get an event ID accepted by the [quorum](../../overview/dictionary) of nodes. An event ID will not be accepted if another node is attempting to assign the same event ID. This is not an issue since the node will just try another event ID. It only indicates the number of collisions occurred while trying to assign an event ID.
events_skipped | Events which cannot be committed since an event with a higher `id` is already processed.
events_unaligned | Number of times an event cannot be pushed to the end of the queue and needs re-ordering.
events_with_gap | Events which are committed but at least one event `id` was skipped.
garbage_collected | Number of [things](../../data-types/thing) which are garbage collected.
largest_result_size | Largest query result size in bytes. Check [node_info()](../node_info) to see the maximum allowed query result size.
longest_event_duration | Longest event duration, in seconds. Event duration is measured from the moment an event is created, until the event is finished. During `AWAY` mode, a node will still create events, but waits before processing events and thus may result in rather long duration values.
longest_query_duration | Longest query duration, in seconds.
queries_from_cache | Number of queries which are loaded from cache.
queries_success | Number of queries where this node acted as the master node and the query has successful finished.
queries_with_error | Number of queries where this node acted as the master node but the query has returned with an error.
started_at | UNIX time-stamp in seconds when the counters started counting. See [reset_counters()](../reset_counters).
wasted_cache | Number of cached queries which are cleaned from the cache without ever being used.
watcher_failed | The value is increased if an update could not be forwarded to a registered watcher.

This function does *not* generate an [event](../../overview/events).

### Function

`counters()`

### Arguments

None

### Return value

Returns the current counter values.

### Example

> This code will return node counter values:

```thingsdb,should_pass,@n
// Returns the current counters for the node in this scope
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
    "largest_result_size": 778,
    "longest_event_duration": 0.000295981,
    "longest_query_duration": 0.000152664,
    "queries_from_cache": 63,
    "queries_success": 159,
    "queries_with_error": 0,
    "started_at": 1590496024,
    "wasted_cache": 9,
    "watcher_failed": 0
}
```
