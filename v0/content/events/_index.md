+++
title = "Events"
date = 2019-10-07T11:01:44+02:00
weight = 4
chapter = true
+++

# Events

When a query uses a statement which makes a change to ThingsDB, then internally ThingsDB will create an *event* to apply these changes.
Events are applied in order on each node so database consistency is guaranteed.
