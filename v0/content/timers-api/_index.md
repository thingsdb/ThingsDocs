---
title: "Timers API"
weight: 282
chapter: true
---

# Timers API

A timer in ThingsDB is a closure that is attached to a scope and runs at a scheduled time. Timers may be configured with a repeat value *(at least 30 seconds)* or as a one-time schedule.

Timers can be used in the `@thingsdb` scope and in `@collection` scopes.

Timers always have a unique Id by which they can be identified.

