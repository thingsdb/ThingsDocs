---
title: "Connect"
weight: 7
chapter: true
---

# Connect

There are several options to communicate with ThingsDB. By default each node listens to port `9200` for TCP socket connections.
With a socket connection it is possible to do queries, run procedures and listen to rooms for events.

The most easy way to use the socket connection is to use an existing *connector*. ThingsDB currently has connectors available for [Python](./python), [Go](./go) and [C#](./csharp).
For other languages you can read the [socket protocol](./socket) section on how to implement a ThingsDB connector.

As an alternative to the socket connection, a ThingsDB node has support for HTTP requests through an [HTTP API](./http-api).
