---
title: "Installation"
weight: 1
chapter: false
---

## From source (linux)

Install dependencies

```
sudo apt-get install -y \
    libuv1-dev \
    libpcre2-dev \
    libmsgpack-dev \
    libyajl-dev
```


At least version `0.11.0` for Library `libcleri` is required.

```
git clone https://github.com/transceptor-technology/libcleri.git
cd libcleri/Release
make
sudo make install
```



First clone the project
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

