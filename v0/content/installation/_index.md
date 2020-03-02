---
title: "Installation"
weight: 1
chapter: false
---

## Try for free

Get your own **playground** for free at [https://thingsdb.net](https://thingsdb.net).

Or.., build your own ThingsDB by cloning the [GitHub](https://github.com/thingsdb/ThingsDB) project and follow the steps below.


## Build from source (linux)

Install the following dependencies:

 - libuv1
 - libpcre2
 - libyajl
 - libcleri (`>=0.12.1`)

When using Debian/Ubuntu; *libuv1*, *libpcre2* and *libyajl* can be installed using apt:
```
sudo apt-get install -y \
    libuv1-dev \
    libpcre2-dev \
    libyajl-dev
```

At least version `0.12.1` for library `libcleri-dev` is required.

```
git clone https://github.com/transceptor-technology/libcleri.git
cd libcleri/Release
make
sudo make install
```

Next, clone the project
```
git clone https://github.com/thingsdb/ThingsDB.git
```

```
cd ThingsDB/Release
make clean && make
```

## Configuration

ThingsDB can start with a configuration file and/or with environment variable.

Variable | Default | Description
-------- | ------- | -----------
`THINGSDB_LISTEN_CLIENT_PORT` | `9200` | Listen on this TCP port for client socket connections.
`THINGSDB_BIND_CLIENT_ADDR` | `0.0.0.0` | Bind client connections to this address. This may also be an IPv6 address like `::`.
`THINGSDB_LISTEN_NODE_PORT` | `9210` | Listen on this TCP port for node connections.
`THINGSDB_BIND_NODE_ADDR` | `0.0.0.0` | Bind node connections to this address. This may also be an IPv6 address like `::`.
`THINGSDB_IP_SUPPORT` | `ALL` | Listen to IPv4 (`IPV4ONLY`), IPv6 (`IPV6ONLY`) or both (`ALL`) addresses.
`THINGSDB_STORAGE_PATH` | *depends* | Location to store ThingsDB data. The default location depends on the user who is running ThingsDB. (`/var/lib/thingsdb/` for *root* and `~/.thingsdb/` for a normal user).
`THINGSDB_PIPE_CLIENT_NAME` | *disabled* | Named PIPE for client connections. Support for client PIPE connections will be disabled if the value is not configured.
`THINGSDB_THRESHOLD_FULL_STORAGE` | `1000` | Threshold for number of events before initiating a full database store.
`THINGSDB_HTTP_STATUS_PORT` | *disabled* | TCP port for listening to health and readiness checks.
`THINGSDB_HTTP_API_PORT` | *disabled* | TCP port for listening to HTTP API calls.
`THINGSDB_ZONE` | `0` | Start node in this zone number. Zones are used for forwarding queries while in *away* mode.
`THINGSDB_QUERY_DURATION_WARN` | *disabled* | Log a warning message when a query takes more than X second(s).
`THINGSDB_QUERY_DURATION_ERROR` | *disabled* | Log an error message when a query takes more than X second(s).


## Add more nodes

ThingsDB can *work* with a single node but is designed to work with at least two nodes but three nodes are preferred.
Running on three nodes brings redundancy and ensures the database stays operational, even while you for example upgrade ThingsDB to a newer version.

See [new_node](../thingsdb-api/new_node) for more information about adding nodes to ThingsDB.

