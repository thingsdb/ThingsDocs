---
title: "node-status"
weight: 393
---

The body of a *Node Status* event contains both the node Id and status of the node.

The status string may be one of the following:

String | Description
------ | -----------
`AWAY_SOON` | The node will enter *away* mode in a few seconds. Unless you really want to act on this state, this notification can be ignored.
`AWAY` | The node is in *away* mode. Unless you really want to act on this state, this notification can be ignored.
`READY` | The node is back to *ready* state. Unless you really want to act on this state, this notification can be ignored.
`SHUTTING_DOWN` | The node will shutdown in a few seconds. This notification may be used to initiate a connection to another node.
`OFFLINE` | The node will be *off-line* after this notification is received.

> Example *node-status* event in JSON format:

```json
{
    "id": 0,
    "status": "READY"
}
```
