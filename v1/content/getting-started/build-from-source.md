---
title: "Build from source"
weight: 2
chapter: false
---

Install the following dependencies:

- libuv1
- libpcre2
- libyajl
- libcleri (`>=0.12.2`)

When using Debian/Ubuntu; *libuv1*, *libpcre2* and *libyajl* can be installed using apt:

```bash
sudo apt-get install -y \
    libuv1-dev \
    libpcre2-dev \
    libyajl-dev
```

At least version `0.12.x` for library `libcleri-dev` is required.

```bash
git clone https://github.com/transceptor-technology/libcleri.git
cd libcleri/Release
make
sudo make install
```

Next, clone the project

```bash
git clone https://github.com/thingsdb/ThingsDB.git
```

```bash
cd ThingsDB/Release
make clean && make
```

You might want to create a symlink like this:

```bash
sudo ln -s ~/ThingsDB/Release/thingsdb /usr/local/bin/thingsdb
```
