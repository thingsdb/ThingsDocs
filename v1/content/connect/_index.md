---
title: "Connect"
weight: 8
chapter: true
---

# Connect

There are several options to communicate with ThingsDB. The easiest option is to use an existing _connector_.

The following connectors are available:

Language                            | Query/Run support | Room (event) support
----------------------------------- | ----------------- | --------------------
[Python](./python)                  | &#x2714;          | &#x2714;
[Go](./go)                          | &#x2714;          | &#x2714;
[C#](./csharp)                      | &#x2714;          | &#x2714;
[PHP](./php)                        | &#x2714;          | &#x2714;
[JavaScript / Node.js](./javascript)| &#x2714;          | &#x2714;
[HTTP (API)](./http-api)            | &#x2714;          | -

For other languages you can read the [socket protocol](./socket) section on how to implement a ThingsDB connector.

As an alternative to the socket connection, a ThingsDB node has support for HTTP requests through an [HTTP API](./http-api).
