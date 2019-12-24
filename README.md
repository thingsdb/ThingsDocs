# The ThingsDB Documentation source


Update golang to version 1.12
```
sudo snap install go --classic
```

Install Hugo (Ubuntu/Debian)

```
sudo snap install hugo
```

Install template
```
git submodule update --init --recursive
```

Start development server
```
hugo server --disableFastRender
```

Build for GitHub pages
```
hugo
```

And upload to master


## Update highlight.js for syntax highlighting

The theme uses highlight.js for syntax highlighting.

Build the custom syntax:

Clone the highlight.js fork:
```
git clone https://github.com/joente/highlight.js.git
```

Build with the required language support
```
cd ./highlight.js
node tools/build.js -n python json thingsdb go bash
```

Copy the build to the Docs project

> Here we assume `ThingsDocs` is a sibling of `highlight.js` in the folder structure
```
cp build/highlight.pack.js ../ThingsDocs/themes/hugo-theme-learn/static/js/highlight.pack.js
```

