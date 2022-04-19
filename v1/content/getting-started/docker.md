---
title: "Docker"
weight: 3
---

### Images

Docker images of ThingsDB are available at [GitHub](https://github.com/thingsdb/ThingsDB/pkgs/container/node/).

**Supported tags**:

`ghcr.io/thingsdb/node:VERSION` _(Minimal ThingsDB image based on Alpine Linux.)_

`ghcr.io/thingsdb/node:gcloud-VERSION` _(Includes Google Cloud Utilities so ThingsDB can created backups in the Google Cloud.)_

`ghcr.io/thingsdb/node:full-VERSION` _(Based on a Debian image with Google Cloud Utilities, Python3 and [py-timod](https://pypi.org/project/py-timod/) installed.)_

`ghcr.io/thingsdb/node:latest` _(Latest ThingsDB build from the `master` branch using a minimal Alpine Linux base image)_

### Getting started

The basic steps required to run the ThingsDB server in Docker are explained below.

#### Pulling

To get started, run the following command in your terminal:

```bash
$ docker pull ghcr.io/thingsdb/node:latest
```

> **Note**: Depending on how you've installed docker on your system, you might see a permission denied error after running the above command. If you're on Linux, you may need to prefix your docker commands with `sudo`. Alternatively you can create a Docker group to get rid of this issue.

The pull command fetches the latest ThingsDB server image from the GitHub Container Registry and saves it in your system.

#### Running

Great! Let's now run a Docker container based on this image. To do that you are going to use the `docker run` command.

```bash
$ docker run --name thingsdb -d -p 9200:9200 -v ~/thingsdb-data:/data -v ~/thingsdb-modules:/modules  ghcr.io/thingsdb/node --init
```

You’ll notice a few flags being used. Here’s some more info on them:

- `-d` - Run the container in detached mode (in the background).
- `-p 9200:9200` - Map port 9200 of the host to port 9200 (ThingsDB port for client socket connections) in the container.
- `-v ~/thingsdb-data:/data` - Mount a volume for ThingsDB data. (For data persistence)
- `-v ~/thingsdb-modules:/modules` - Mount a volume for ThingsDB modules. (For data persistence)
- `ghcr.io/thingsdb/node` - The image to use.
- `--init` - For initializing ThingsDB. This argument is technically only required when running ThingsDB for the first time.

To verify that the container is running, you can use the `docker ps` command.

```bash
$ docker ps
```

This command shows you all containers that are currently running and should display a similar output as this:

```bash
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS         PORTS                                                                     NAMES
408e414a0213   ghcr.io/thingsdb/node   "/usr/local/bin/thin…"   9 seconds ago   Up 8 seconds   8080/tcp, 9210/tcp, 9220/tcp, 0.0.0.0:9200->9200/tcp, :::9200->9200/tcp   thingsdb
```

#### Stopping

To stop the active ThingsDB container, run the `docker stop` command.

```bash
$ docker stop thingsdb
```
