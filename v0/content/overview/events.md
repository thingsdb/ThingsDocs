---
title: "Events"
weight: 20
---

When a query uses a statement which makes a change to ThingsDB, then internally ThingsDB will create an *event* to apply these changes.
Events are applied in order on each node so database consistency is guaranteed.

A single query might contain several statements and make many changes. All changes within a query will be grouped in a single event.

{{% notice tip %}}
In the documentation we try to make clear if a function will generate an event or not. If you only want to *read* information from ThingsDB,
you should try to avoid functions which generate an event. Functions on a [list](../../data-types/list) or [set](../../data-types/set)
do *not* create an event when called on a [variable](../variable).
{{% /notice %}}