---
title: "Watching"
weight: 185
chapter: false
---

Socket connections can receive push notifications from ThingsDB. Push notification do only work when using a socket connection and cannot be used with the HTTP API.

Before notification are received you have to *subscribe* for changes.


Notifications which may be received by a client:

Notification | Description
------------ | -----------
[NODE_STATUS](./node-status) (`0`) | The connected node has changed its status.
[ON_INIT](./on-init) (`1`) | Initial data for the [thing](../data-types/thing) which is added to the watch list.
[ON_UPDATE](./on-update) (`2`) | Update on a [thing](../data-types/thing) is the watch list.
[ON_DELETE](./on-delete) (`3`) | A [thing](../data-types/thing) from the watch list is removed.
[WARNING](./warning) (`4`) | A warning message.

> The number `0-4` represents the package type in a [package header](http://localhost:1313/v0/connect/socket/#package).


TODO: explain how to subscribe