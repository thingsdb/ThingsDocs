---
title: "regex"
weight: 41
---

Regular expression can be constructed using a literal which consists of a pattern enclosed between slashes, as follows: `re = /ab+c/;`.
It is probably a good idea to store a `regex` in a variable if you plan to use the regular expression multiple times. This prevents the
requirement to compile the regular expression each time.

### Methods that use regular expressions

Method | Description
------ | -----------
[test](../../data-types/str/test) | A [str](../../data-types/str) method that tests for a match in a string. It returns `true` or `false`.

> This code uses a regular expression for an overly simple email check:

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