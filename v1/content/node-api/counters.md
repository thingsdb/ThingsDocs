---
title: "counters"
weight: 288
---

Returns `counters` for the ThingsDB node in the selected scope. Counters start all at zero when ThingsDB
is started, or when the counters are reset by using [reset_counters()'](../reset_counters).

Counters give information about things, queries and changes. If you suspect failed queries, then
the counters might provide you with more information.

Counter | Description
------- | -----------
average_change_duration | The average [change](../../overview/changes) duration in seconds. Change duration is measured from the time a *change* is created *(before the final Id is assigned)*, until the actual *change* is committed to ThingsDB.
average_query_duration | The average query duration in seconds. Query duration is measured from the time a query *(or procedure run)* request is unpacked, until the response is created to send back to the client.
changes_committed | [Changes](../../overview/changes) committed since last the counters reset.
changes_failed | Failed changes. This is a *critical* counter which should be `0`.
changes_killed | Killed changes took too long for receiving the `READY` status. These changes may be processed later.
changes_skipped | Changes which cannot be committed since a *change* with a higher `id` is already processed.
changes_unaligned | Number of times a *change* cannot be pushed to the end of the queue and needs re-ordering.
changes_with_gap | Changes which are committed but at least one *change-Id* was skipped.
garbage_collected | Number of [things](../../data-types/thing) which are garbage collected.
largest_result_size | Largest query result size in bytes. Check [node_info()](../node_info) to see the maximum allowed query result size.
longest_change_duration | Longest change duration, in seconds. Change duration is measured from the moment a *change* is created, until the change is finished. During `AWAY` mode, a node will still create changes, but waits before processing changes and thus may result in rather long duration values.
longest_query_duration | Longest query duration, in seconds.
queries_from_cache | Number of queries which are loaded from cache.
queries_success | Number of queries where this node acted as the master node and the query has successful finished.
queries_with_error | Number of queries where this node acted as the master node but the query has returned with an error.
quorum_lost | Number of times this node did not get a *change* Id accepted by the [quorum](../../overview/dictionary) of nodes. a *change-Id* will not be accepted if another node is attempting to assign the same *change-Id*. This is not an issue since the node will just try another *change-Id*. It only indicates the number of collisions occurred while trying to assign a *change* Id.
started_at | UNIX time-stamp in seconds when the counters started counting. See [reset_counters()](../reset_counters).
tasks_success | Number of successfully processed tasks.
tasks_with_error | Number of processed tasks where the task returned with an error.
wasted_cache | Number of cached queries which are cleaned from the cache without ever being used.

This function does *not* generate a [change](../../overview/changes).

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
    "average_change_duration": 0.032120732,
    "average_query_duration": 0.009859586882352942,
    "changes_committed": 1,
    "changes_failed": 0,
    "changes_killed": 0,
    "changes_skipped": 0,
    "changes_unaligned": 0,
    "changes_with_gap": 0,
    "garbage_collected": 0,
    "largest_result_size": 1247,
    "longest_change_duration": 0.032120732,
    "longest_query_duration": 0.066440648,
    "queries_from_cache": 1,
    "queries_success": 17,
    "queries_with_error": 0,
    "quorum_lost": 0,
    "started_at": 1627903017,
    "tasks_success": 0,
    "tasks_with_error": 0,
    "wasted_cache": 0,
    "watcher_failed": 0
}
```
