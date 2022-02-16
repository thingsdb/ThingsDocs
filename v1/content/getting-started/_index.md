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

Docker images are available at [GitHub](https://github.com/thingsdb/ThingsDB/pkgs/container/node/).


Supported tags:

`ghcr.io/thingsdb/node:VERSION` *(Minimal ThingsDB image based on Alpine Linux.)*

`ghcr.io/thingsdb/node:gcloud-VERSION` *(Includes Google Cloud Utilities so ThingsDB can created backups in the Google Cloud.)*

`ghcr.io/thingsdb/node:full-VERSION` *(Based on a Debian image with Google Cloud Utilities, Python3 and [py-timod](https://pypi.org/project/py-timod/) installed.)*

`ghcr.io/thingsdb/node:latest` *(Latest ThingsDB build from the `master` branch using a minimal Alpine Linux base image)*


### Run ThingsDB in GKE (Google Kubernetes Engine)

The following link will explain how to deploy ThingsDB in GKE (Google Kubernetes Engine):

[https://github.com/thingsdb/ThingsDB/tree/master/gke#readme](https://github.com/thingsdb/ThingsDB/tree/master/gke#readme)