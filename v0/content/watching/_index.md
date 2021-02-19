---
title: "Watching"
weight: 283
chapter: false
---

Socket connections can receive events from ThingsDB. Push events do only work when using a socket connection and cannot be used with the HTTP API.

Before events are received you have to *subscribe* for changes.

The following events may be received by a client:

Event | Description
------------ | -----------
[NODE_STATUS](./node-status) (`0`) | The connected node has changed its status.
[ON_INIT](./on-init) (`1`) | Initial data for the [thing](../data-types/thing) which is added to the watch list.
[ON_UPDATE](./on-update) (`2`) | Update on a [thing](../data-types/thing) in the watch list.
[ON_DELETE](./on-delete) (`3`) | A [thing](../data-types/thing) in the watch list is removed.
[ON_STOP](./on-stop) (`4`) | A [thing](../data-types/thing) is no longer being watched.
[WARNING](./warning) (`5`) | A warning message.

> The number `0-5` represents the package type in a [package header](http://localhost:1313/v0/connect/socket/#package).

## Subscribe for node status changes

For receiving [NODE_STATUS](./node-status) events you need to sent a  [watch request](../connect/socket/watch) to the `@node` scope. At least `WATCH` permissions for the `@node` scope are required.

When using a client, this is pretty easy, for example using the Python client:

```python
await client.watch('@node')
```

If you want to write the request to the socket connection yourself, sending the following byte data on your socket connection will have the same result:

```none
\x07\x00\x00\x00\x00\x00\x23\xdc\x91\xa5@node
```

(See the *"creating a [watch request](../connect/socket/watch) example"* on how we got the above bytes code)

## Subscribe for thing mutations

If you start to watch a thing, the following events will be pushed in order:

- [ON_INIT](./on-init), This event will **always** be pushed on each watch request.
- [ON_UPDATE](./on-update), You receive an update event for each **mutation** after the *initial* [ON_INIT](./on-init) event.
- [ON_DELETE](./on-delete) or [ON_STOP](./on-stop), No more events will be pushed for the thing after this event.

To start watching one or more things, a [watch request](../connect/socket/watch) may be used, but as an alternative it is also
possible to use the functions [watch()](../data-types/thing/watch) and [unwatch](../data-types/thing/unwatch). There is no
alternative function for watching the node status.
