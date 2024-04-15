---
title: "JavaScript"
weight: 14
---

### Requirements

- ThingsDB [v1.6.0](https://docs.thingsdb.io/v1/)
- Javascript

### Installation

This library is available for both frontend and backend. You should choose installation method by your need.

#### browser
Package is automatically available at unpkg. You can find latest version of package at https://unpkg.com/thingsdb.js@latest/dist/thingsdb.js

Add this into your html head:
```
<script src="https://unpkg.com/thingsdb.js@latest/dist/thingsdb.js"></script>
```

#### npm
Package is available at npm [https://www.npmjs.com/package/thingsdb.js](https://www.npmjs.com/package/thingsdb.js)

Run this command to install package into your project:
```
npm i thingsdb.js
```

### Example

```php
const thingsdb = new ThingsDB('ws://localhost:9270');
thingsdb.connect().then(() => {
    thingsdb.auth().then(() => {
        thingsdb.query('@:stuff', '"Hello World!";').then(response => {
            console.log(response); // will be "Hello World!"
        });
    });
});
```

### More info

A more complete description of the JavaScript/Node.js connector can be found in the link below.

- https://github.com/stefanak-michal/thingsdb.js#readme
