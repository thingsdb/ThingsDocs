---
title: "Installation"
weight: 1
chapter: false
---

## Try for free

Get your own **playground** for free at [http://thingsdb.net](http://thingsdb.net).

Or.., build your own ThingsDB by cloning the [GitHub](https://github.com/thingsdb/ThingsDB) project and following one of the description


## Build from source (linux)

Install the following dependencies:

 - libuv1
 - libpcre2
 - libyajl
 - libmsgpack (`>=3.2.0`)
 - libcleri (`>=0.11.0`)

When using Debian/Ubuntu, *libuv1*, *libpcre2* and *libyajl* can be installed using apt:
```
sudo apt-get install -y \
    libuv1-dev \
    libpcre2-dev \
    libyajl-dev
```

At least version `3.2.0` for library `libmsgpack-dev` is required.

> It does not seem to work with `3.0.x` which is currently shipped with Ubuntu

```
git clone https://github.com/msgpack/msgpack-c.git
cd msgpack-c
cmake .
make
sudo make install
```

At least version `0.11.0` for library `libcleri-dev` is required.

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
make
```

## Configuration

ThingsDB can start with a configuration file and/or with environment variable.


## Add more nodes

ThingsDB can *work* with a single node but is designed to work with at least two nodes but three nodes are preferred.
Running on three nodes brings redundancy and ensures the database stays operational, even while you for example upgrade ThingsDB to a newer version.

See [new_node](../thingsdb-api/new_node) for more information about adding nodes to ThingsDB.

