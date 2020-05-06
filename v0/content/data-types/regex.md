---
title: "regex"
weight: 61
---

Regular expression can be constructed using a literal which consists of a pattern enclosed between slashes, as follows: `re = /ab+c/;`.
It is probably a good idea to store a `regex` in a variable if you plan to use the regular expression multiple times. This prevents the
requirement to compile the regular expression each time.

### Functions that use regular expressions

Function | Description
------ | -----------
[test](../../data-types/str/test) | A [str](../../data-types/str) function`true` or `false`.

> This code uses a regular expression for an oversimplified email check:

```thingsdb,json_response
// Note: the email check is oversimplified, do not use in production
email_test = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;

/* example usage of our 'email_test' */
email = 'info@thingsdb.net';
email.test( email_test );
```

> Return value in JSON format

```json
true
```
