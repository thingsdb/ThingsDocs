---
title: "Connect"
weight: 2
chapter: true
---

# Connect

There are several options to communicate with ThingsDB. By default each node listens to port `9200` for TCP socket connections.
With a socket connection it is possible to do queries, run procedures and *watch* for changes made to individual things in a collection.

The most easy way to use the socket connection is to use an existing *connector*. ThingsDB currently has connectors available for [Python](./python) and [Go](./go).
For other languages you can read the [protocol](./protocol) section on how to implement a ThingsDB connector.

As an alternative to the socket connection, a ThingsDB node has support for HTTP request through a [HTTP API](./http-api).
This HTTP API listens be default to port `9210` but can be desabled or changed with the `http_api_port` in the configuration file or with the `THINGSDB_HTTP_API_PORT` environment variable.
