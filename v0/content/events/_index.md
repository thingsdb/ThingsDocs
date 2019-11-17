---
title: "Events"
weight: 4
chapter: true
---

# Events

When a query uses a statement which makes a change to ThingsDB, then internally ThingsDB will create an *event* to apply these changes.
Events are applied in order on each node so database consistency is guaranteed.

A single query might contain several statements and make many changes. All changes within a query will be grouped in a single event.