---
title: "String (raw)"
date: 2019-10-14T09:40:11+02:00
weight: 10
---

ThingsDB has only type `raw` which is used for storing both *strings* and *blob* values.

### Methods
Method | Description
------ | -----------
[endswith](../../collection-api/endswith) | Determines if a string ends with characters given by another string.
[len](../../collection-api/len) | Returns the length of a string.
[lower](../../collection-api/lower) | Return a new string in which all case-based characters are in lower case.
[startswith](../../collection-api/startswith) | Determines if a string starts with characters given by another string.
[test](../../collection-api/test) | Test if a string matches a given regular expression and return `true` or `false`.
[upper](../../collection-api/upper) | Return a new string in which all case-based characters are in upper case.

> This code creates a *raw* property *greet* to collection *stuff*:

```
greet = 'Hello world!!';
```
