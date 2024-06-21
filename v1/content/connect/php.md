---
title: "PHP"
weight: 14
---

### Requirements

- ThingsDB [v1](https://docs.thingsdb.io/v1/)
- PHP ^8.2
- [rybakit/msgpack](https://github.com/rybakit/msgpack.php)
- [mbstring](https://www.php.net/manual/en/book.mbstring.php)
- [openssl](https://www.php.net/manual/en/book.openssl.php) - Required only for connection with enabled SSL

### Installation

Run the following command in your project to install the latest applicable version of the package:

```
composer require stefanak-michal/thingsdb-php
```

### Quick usage

```php
use ThingsDB\ThingsDB;

$thingsDB = new ThingsDB();
$result = $thingsDB->auth(); // returns true on success
$message = $thingsDB->query('@:stuff', '"Hello World!";'); // returns "Hello World!"
```

### More info

A more complete description of the PHP connector can be found in the link below.

- https://github.com/stefanak-michal/thingsdb-php#readme
