---
title: "Changes"
weight: 27
---

When a query uses a statement which makes a change to ThingsDB, then internally ThingsDB will create a *change* with a new *change-Id* to apply these transformations.
Changes are applied in order on each node; so database consistency is guaranteed.

A single query might contain several statements and make many changes. All changes within a query will be grouped in a single *change* with the exception of future callbacks. Each future callback will get its own *change-Id* if a *change* is required (see the [future type](../../data-types/future) for more info on futures).

{{% notice tip %}}
In the documentation we try to make clear if a function will generate a *change* or not. If you only want to *read* information from ThingsDB,
you should try to avoid functions which generate a *change*. Functions on a [list](../../data-types/list) or [set](../../data-types/set)
do *not* create a *change* when called on a [variable](../variable).
{{% /notice %}}
