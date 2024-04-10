---
title: "Build from source"
weight: 2
chapter: false
---

First, install the following required dependencies:

- libuv1
- libpcre2
- libyajl
- libcurl

When using Debian/Ubuntu; _libuv1_, _libpcre2_, _libyajl_ and _libcurl_ can be installed using apt:

```bash
sudo apt-get install -y \
    libuv1-dev \
    libpcre2-dev \
    libyajl-dev \
    libcurl4-nss-dev \
```

Next, clone the ThingsDB project.

```bash
git clone https://github.com/thingsdb/ThingsDB.git
```

Make sure the build essentials (and cmake) are installed.

For Debian/Ubuntu:

```bash
sudo apt-get install build-essential cmake
```

Then compile the source code to make it executable.

```bash
./ThingsDB/release-build.sh
```

Finally, you might want to create a symlink like this:

```bash
sudo ln -s ~/ThingsDB/thingsdb /usr/local/bin/thingsdb
```
