---
title: "Timers API"
weight: 282
chapter: true
---

# Timers API

A timer in ThingsDB is a closure that is attached to a scope and runs at a scheduled time. Timers may be configured with a repeat value *(at least 30 seconds)* or as a one-time schedule.

Timers can be used in the `@thingsdb` scope and in `@collection` scopes.

Timers always have a unique Id by which they can be identified.


### Related functions

Function | description
-------- | ----- | -----------
[del_timer](./del_timer) | Delete an existing timer.
[has_timer](./has_timer) | Check if a timer exists.
[new_timer](./new_timer) | Create a new timer.
[run](./run) | Run a timer *(runs the closure with the timer arguments)*.
[set_timer_args](./set_timer_args) | Change timer arguments.
[timer_args](./timer_args) | Get the current timer arguments.
[timer_info](./timer_info) | Show information about a timer.
[timers_info](./timers_info) | Show information about all timers in the current scope.
