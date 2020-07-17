---
title: "Getting started"
weight: 1
chapter: true
---

# Getting started

### Try for free

Get your own **playground** for free at [https://thingsdb.net](https://thingsdb.net) and continue reading at [connect](../connect).

Or.., build your own ThingsDB by cloning the [GitHub](https://github.com/thingsdb/ThingsDB) project and follow the steps in the next paragraphs.

### Docker images

Docker images are available at [docker hub](https://hub.docker.com/r/thingsdb/node).


Each version has two images:

A minimal ThingsDB image (using Alpine Linux)

```
thingsdb/node:v0.x.x
```

And one with the Google Cloud SDK installed so ThingsDB can created backups in the Google Cloud

```
thingsdb/node:gcloud-v0.x.x
```

