---
title: "regex"
weight: 89
---

Regular expression can be constructed using a literal which consists of a pattern enclosed between slashes, as follows: `re = /ab+c/;`.
It is probably a good idea to store a `regex` in a variable if you plan to use the regular expression multiple times. This prevents the
requirement to compile the regular expression each time.

### Flags

Flag | Description
---- | -----------
`i`  | Case-insensitive search.
`m`  | Multi-line search.
`s`  | Allows `.` to match newline characters.

### Functions

Function | Description
------ | -----------
[test](./test) | Test if a given [string](../str) has a match with the regular expression.


### Related functions

Function | Description
------ | -----------
[is_regex](../../collection-api/is_regex) | Test if a given value is of type `regex`.
[regex](../../collection-api/regex) | Create a new `regex`.
*str.*[replace](../str/replace) | Replace one or more occurrences of a `regex` pattern in a string.
*str.*[split](../str/split) | Split a string based on a `regex` pattern.


> This code uses a regular expression for an oversimplified email check:

```thingsdb,json_response
// Note: the email check is oversimplified, do not use in production
email_test = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;

/* example usage of our 'email_test' */
email_test.test('info@thingsdb.net');
```

> Return value in JSON format

```json
true
```
