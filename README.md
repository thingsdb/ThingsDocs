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

> With the latest version of Hugo, the menu seems to be broken.

A working version (including a .deb file) can be downloaded [here](https://github.com/gohugoio/hugo/releases/tag/v0.90.0).

Install template

```bash
git submodule update --init --recursive
```

## Usage

To start the website run the following commands:

**Development**:

Start development server from the `v1/` folder. (or `v0/` for the previous mayor ThingsDB version documentation)

```bash
hugo server --disableFastRender # This command starts the Hugo server and watches the site directory for changes.
```

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
cp build/highlight.js ../ThingsDocs/themes/hugo-theme-learn/static/js/highlight.pack.js
```

## Adding a chapter or paragraph

When you like to add another document to the content, it needs a weight value. The weight value determines the ordering of the files. This means that when a file is added at the beginning, the weight value of all the files that follow needs to be changed. This process can be time consuming, therefore we made a python script that does this for you.

After the file is added run the next command:

```bash
./weight_map.py --export > site.map
```

Now the site.map is created. Open this file. You will see all the chapters and paragraphs. Check if the order from top to down is correct. Otherwise you can change it in this file.

Next run the following command:

```bash
./weight_map.py --apply site.map
```

The weight value of all files has been updated according to the order in the site.map file.
