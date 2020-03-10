# ThingsDB - Docs

This is the repository for the ThingsDB documentation. It makes use of the Hugo Learn theme and Hugo.

## Prerequisites

- [Install Git](https://git-scm.com/downloads).
- [Install Go](https://golang.org/doc/install).
- [Install Hugo](https://gohugo.io/getting-started/installing/). Depending on the system, this might require Scoop, Chocolatey, or other software.

Update golang to version 1.12

```bash
sudo snap install go --classic
```

Install Hugo (Ubuntu/Debian)

```bash
sudo snap install hugo
```

Install template

```bash
git submodule update --init --recursive
```

## Usage

To start the website run the following commands:

**Development**:

Start development server

```bash
hugo server --disableFastRender # This command starts the Hugo server and watches the site directory for changes.
```

**Production**:

Build for GitHub pages

```bash
hugo # This command generates the static website in the public/ directory. If you do not have a site, then it gives errors about missing layout files.
```

And upload to master

## Syntax highlighting

The theme uses highlight.js for syntax highlighting.

Build the custom syntax:

Clone the highlight.js fork:

```bash
git clone https://github.com/thingsdb/highlight.js.git
```

Build with the required language support

```bash
// Go to the highlight.js folder
cd ./highlight.js

// Make sure you have Node.js installed and get the dependencies
npm install

//Build the included languages and skip compression in this case
node tools/build.js -n python json thingsdb go bash
```

Copy the build to the Docs project

> Here we assume `ThingsDocs` is a sibling of `highlight.js` in the folder structure

```bash
cp build/highlight.pack.js ../ThingsDocs/themes/hugo-theme-learn/static/js/highlight.pack.js
```
