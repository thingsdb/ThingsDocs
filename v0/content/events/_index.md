---
title: "Events"
weight: 13
chapter: true
---

# Events

When a query uses a statement which makes a change to ThingsDB, then internally ThingsDB will create an *event* to apply these changes.
Events are applied in order on each node so database consistency is guaranteed.

A single query might contain several statements and make many changes. All changes within a query will be grouped in a single event.

{{% notice tip %}}
In the documentation we try to make clear if a function will generate an event or not. If possible, you should try to avoid a query to make an
event if you do not intent to make changes which need to be stored.
{{% /notice %}}